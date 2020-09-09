import json, datetime, time, io, math
from PIL import Image

from utils import ResizeImage
from config import S3

class ProductService:

    def __init__(self, product_dao):
        self.product_dao = product_dao

    def create_product(self, product_info, db_connection):

        """

        상품등록 - Business Layer(service) function

        Args:
            product_info  : 로 받은 Parameter
                mainCategoryId    : Main Category ID
                subCategoryId     : Sub Category ID
                sellYn            : 상품 판매여부 (Boolean)
                exhibitionYn      : 상품 진열여부 (Boolean)
                productName       : 상품이름
                simpleDescription : 상품 한 줄 설명
                detailInformation : 상품 상세 설명
                price             : 상품가격
                discountRate      : 상품 할인율
                discountStartDate : 할인 시작일
                discountEndDate   : 할인 종료일
                minSalesQuantity  : 최소판매 수량
                maxSalesQuantity  : 최대판매 수량
                optionQuantity    : 옵션별 수량 List
                {
                    colorId  : 상품 색상 id
                    sizeId   : 상품 사이즈 id
                    quantity : 상품 재고수량
                }

            db_connection : DATABASE Connection Instance

        Returns :
            product_id : products Table의 PK

        Author :
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-25 (sincerity410@gmail.com) : 초기생성
            2020-08-26 (sincerity410@gmail.com) : controller, service, model role 재정의에 따른 함수수정
            2020-08-28 (sincerity410@gmail.com) : images, product_images insert 수행
            2020-08-30 (sincerity410@gmail.com) : option 별 재고수량 관련 테이블(product_options, option_details,
                                                  quantities) insert 수행
            2020-09-02 (sincerity410@gmail.com) : product_code(unique 값)의 insert로 구조 수정

        """

        # 선분 관리할 시간 저장
        now = self.product_dao.select_now(db_connection)
        product_info['now'] = now

        # product에 insert 한 id를 product_info에 포함 > 상세정보 insert query 실행
        product_info['product_id'] = self.product_dao.insert_product(db_connection)
        self.product_dao.insert_product_detail(product_info, db_connection)

        # nested JSON 구조인 optionQuantity를 form-data로 받아 JSON 변환
        options = json.loads(product_info['optionQuantity'])

        # 상품 옵션 별 produc_options, option_details, quantities 테이블 insert 수행 
        for option in options :
            product_option_id  = self.product_dao.insert_product_option(product_info['product_id'], db_connection)
            color_id           = self.product_dao.select_color_id(option, db_connection)
            size_id            = self.product_dao.select_size_id(option, db_connection)
            option['color_id'] = color_id
            option['size_id']  = size_id
            option_detail_id   = self.product_dao.insert_option_detail(now, product_option_id, option, db_connection)
            self.product_dao.insert_quantity(option_detail_id, option, db_connection)

        # Image S3 Upload 및 RDB에 URL Link insert를 위해 product_id return
        return product_info['product_id']

    def get_product_list(self, db_connection):

        """

        브랜디 서비스 페이지 > 상품 전체 리스트

        Args:
            db_connection : 연결된 db 객체

        Returns:
            상품 전체 리스트

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-08-25 (minho.lee0716@gmail.com) : 초기 생성

        """

        # 상품의 기준은 진열여부=True, 판매여부=True
        products = self.product_dao.select_product_list(db_connection)

        for product in products:
            product['sales_price'] = round(product['original_price'] * (100-product['discount_rate'])/ 100, -1)

        # 모든 상품을 리턴
        return products

    def upload_product_image(self, images, product_id, s3_connection, db_connection):

        """

        상품 이미지 등록 - Business Layer(service) function

        Args:
            images        : File Request(List)
                [
                    { 'product_image_<int>' : <FileStorage: {filename} ({content_type})>}
                ]
            s3_connection : S3 Connection Instance

        Returns:
            None

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-27 (sincerity410@gmail.com) : 초기생성
            2020-09-02 (sincerity410@gmail.com) : product_code 추가에 따른 구조 수정

        """

        # product image
        product_images = {}

        try:
            for idx in range(1,6):

                # 대표사진 미등록 시 예외처리
                if 'product_image_1' not in images :
                    raise Exception('THUMBNAIL_IMAGE_IS_REQUIRED')

                # 상품사진 미정렬 시 예외처리
                if idx > 2  :
                    if (f'product_image_{idx}' in images) and (f'product_image_{idx-1}' not in images) :
                        raise Exception('IMAGE_CAN_ONLY_REGISTER_IN_ORDER')

                # 상품사진 있는 경우 product_images Dictionary에 저장
                if f'product_image_{idx}' in images :
                    product_images[images[f'product_image_{idx}'].name] = images.get(f'product_image_{idx}', None)

                    # 파일이 Image가 아닌 경우 Exception 발생
                    image         = Image.open(product_images[f'product_image_{idx}'])
                    width, height = image.size

                    # 사이즈가 너무 작은 경우 예외처리
                    if width < 640 or height < 720 :
                        raise Exception('IMAGE_SIZE_IS_TOO_SMALL')

            # image file name에 등록되는 product_code 조회
            product_code = self.product_dao.select_product_code(product_id, db_connection)

            # 상품 이미지 받아오기 및 유효성 검사 이후 S3 upload
            resizing      = ResizeImage(product_code['product_code'], product_images, s3_connection)
            resized_image = resizing()

            # 사진크기 별 product_image(최대 5개)에 대해 image URL insert & product_images(매핑테이블) insert
            for product_image_no, image_url in resized_image.items() :
                image_no = self.product_dao.insert_image(image_url, db_connection)
                self.product_dao.insert_product_image(product_id, image_no, product_image_no, db_connection)

            return None

        except Exception as e:
            raise e

    def get_option_list(self, db_connection) :

        """

        옵션(색상, 사이즈) 목록을 List로 Return 하는Business Layer(service) function

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            "data": [
                "color":[
                    {
                        "color_no" : {color_no} ,
                        "name"     : "{color_nam}"
                    }
                ]
                "size":[
                    {
                        "size_no" : {size_no},
                        "name"    : "{size_name}"
                    }
                ]
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성
            2020-09-02 (sincerity410@gmail.com) : 상품 옵션정보(색상, 사이즈) 통합

        """

        # DB connection으로 각 옵션 정보 Return 하는 함수 호출
        colors = self.product_dao.select_color_list(db_connection)
        sizes  = self.product_dao.select_size_list(db_connection)

        # 모든 옵션 정보 Return
        return {'color' : colors, 'size' : sizes}

    def get_main_category_list(self, db_connection) :

        """

        Main Category 목록을 Return 하는Business Layer(service) function

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            "data": [
                {
                  "main_category_no" : {main_category_id},
                  "name"             : "{main_category_name}"
                }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-30 (sincerity410@gmail.com) : 초기생성

        """

        # DB connection으로 사이즈 정보 Return 하는 select_size_list 함수 호출
        main_categories = self.product_dao.select_main_category_list(db_connection)

        # 모든 Main Category 정보 Return
        return main_categories

    def get_sub_category_list(self, main_cetegory_id, db_connection) :

        """

        Sub Category 목록을 Return 하는Business Layer(service) function

        Args:
            main_cetegory_id : main_categories 테이블의 PK
            db_connection    : DATABASE Connection Instance

        Returns:
            "data": [
                {
                  "name"            : "{sub_category_name}",
                  "sub_category_no" : {sub_category_no}
                }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-30 (sincerity410@gmail.com) : 초기생성

        """

        # DB connection으로 사이즈 정보 Return 하는 select_size_list 함수 호출
        sub_categories = self.product_dao.select_sub_category_list(main_cetegory_id, db_connection)

        # 모든 Main Category 정보 Return
        return sub_categories

    def get_product_details(self, product_id, db_connection):

        """

        상품 상세정보 > 이미지들

        Args:
            product_id : 상품 고유의 id(pk)
            db_connection : 연결된 db 객체

        Returns:
            해당 상품의 이미지들

        Authors:
            minho.lee0716@gmail.com (이민호)
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-27 (minho.lee0716@gmail.com) : 초기 생성
            2020-08-30 (minho.lee0716@gmail.com) : 이미지 리스트를 details에 추가.
            2020-08-31 (minho.lee0716@gmail.com) : 상품 옵션들을 details에 추가.
            2020-09-01 (minho.lee0716@gmail.com) : 상품 옵션들중 색상만 주는걸로 변경.
            2020-09-01 (minho.lee0716@gmail.com) : 이미지나 색상이 없을 경우 빈 배열을 리턴하도록 수정.
            2020-09-09 (tnwjd060124@gmail.com) : 상품 id에 해당하는 제품이 없는 경우 다른 정보를 가져오지 않도록 처리

        """

        # 해당 상품의 아이디를 받아 상세정보들을 가져옴.
        # 상세정보중 이미지들과 옵션들은 따로 가져와서 details에 추가.
        details = self.product_dao.select_product_details(product_id, db_connection)

        # 상품 아이디에 해당하는 제품이 존재하는 경우
        if details:

            details['image_list'] = self.product_dao.select_product_images(product_id, db_connection)
            details['colors']     = self.product_dao.select_product_option_colors(product_id, db_connection)

            # 할인 가격 계산
            details['sales_price'] = round(details['original_price'] * (100-details['discount_rate'])/ 100, -1)

            # 이미지가 없을 때, (배열 안에 null이 들어 있습니다.)
            # 첫번째 요소가 null이면 빈 배열 반환
            if not details['image_list'][0]:
                details['image_list'] = []

            # 마찬가지로 색상이 없을 경우, 빈 배열을 리턴
            if not details['colors'][0]:
                details['colors'] = []

            # 해당 상품의 상세정보들을 리턴
        return details

    def get_etc_options(self, product_info, db_connection):

        """

        상품 상세정보에서 색상 선택시 컬러를 리턴

        Args:
            product_id    : 상품 고유의 id(pk)
            color_name    : 상품 색상의 이름
            db_connection : 연결된 db 객체

        Returns:
            해당 상품의 이미지들

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-09-01 (minho.lee0716@gmail.com) : 초기 생성
            2020-09-01 (minho.lee0716@gmail.com) : 상품 옵션에서 색상을 받으면 사이즈를 리턴
            2020-09-01 (minho.lee0716@gmail.com) : 상품에 해당 색상이 없을 시 에러 처리

        """

        try:

            # 해당 상품의 아이디를 받아 상세정보들을 가져옴.
            etc_options = self.product_dao.select_etc_options(product_info, db_connection)

            # 해당 상품의 색상이 존재하지 않을 경우
            if not etc_options:
                raise Exception('THIS_COLOR_DOES_NOT_EXISTS')

            # 해당 상품의 상세정보들을 리턴
            return etc_options

        except Exception as e:
            raise e

    def get_registered_product_list(self, filter_info, db_connection) :

        """

        Filtering을 통한 상품 List와 Total Count를 Return 하는Business Layer(service) function

        Args:
            product_info:
                sellYN       : 판매 여부
                exhibitionYn : 진열 여부
                discountYn   : 할인 여부
                registDate   : 등록 일자(기준 시작일, 기준 종료일)
                {
                    startDate : "YYYYmmdd",
                    endDate   : "YYYYmmdd"
                }
                productName  : 상품 이름
                productNo    : 상품 번호
                productCode  : 상품 코드
                limit        : 페이지 당 상품 수
                page         : 페이지 리스트 시작 기준

            db_connection    : DATABASE Connection Instance

        Returns:
            data: [
                [
                    {
                        discountPrice        : 할인가
                        discountRate         : 할인율
                        discountYn           : 할인 여부
                        productCode          : 상품 코드
                        productExhibitYn     : 진열 여부
                        productName          : 상품 이름
                        productNo            : 상품 번호
                        productRegistDate    : 상품 등록 일시
                        productSellYn        : 판매 여부
                        productSmallImageUrl : SMALL SIZE IMAGE URL
                        sellPrice            : 상품 가격
                    }
                ],
                    {
                        "total": 검색된 상품 개수
                    }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-02 (sincerity410@gmail.com) : 초기생성

        """

        # page 값으로 offset 정보 획득
        filter_info['offset'] = filter_info['page'] * filter_info['limit'] - filter_info['limit']

        # DB connection으로 (상품 List & Total Count) Return 하는 select_registered_product_list 함수 호출
        product_list = self.product_dao.select_registered_product_list(filter_info, db_connection)

        return product_list

    def upload_detail_image(self, image, s3_connection):

        """

        상품 상세 이미지 등록 - Business Layer(service) function

        Args:
            image         : File Request
                {'product_detail_image' : <FileStorage: {filename} ({content_type})>}
            s3_connection : S3 Connection Instance

        Returns:
            image URL

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-03 (sincerity410@gmail.com) : 초기생성
            2020-09-04 (sincerity410@gmail.com) : 추가 수정(CKEditor 형식에 맞춰 Return)

        """

        try:
            # 사진 미등록 시 예외처리
            if 'upload' not in image :
                raise Exception('IMAGE_IS_REQUIRED')

            detail_image = image.get('upload')

            # 파일이 Image가 아닌 경우 Exception 발생
            opend_image   = Image.open(detail_image)
            width, height = opend_image.size

            # 사이즈가 너무 작은 경우 예외처리
            if width < 1000:
                raise Exception('IMAGE_SIZE_IS_TOO_SMALL')

            # buffer 초기화
            buffer = io.BytesIO()
            opend_image.save(buffer, "JPEG")
            buffer.seek(0)

            # image file name 설정: detail_yyyy_mm_dd_{unix_time_stamp}
            time_now  = datetime.datetime.now()
            file_name = f"detail/{time_now.year}/{time_now.month}/{time_now.day}/{int(time.time())}"

            # S3 Push
            s3_connection.put_object(
                Body        = buffer,
                Bucket      = 'brandi-project',
                Key         = file_name,
                ContentType = detail_image.content_type
            )

            # Return 할 URL
            detail_image_url = f"{S3['aws_url']}{file_name}"

            image_url_info = {}

            image_url_info['uploaded'] = 1
            image_url_info['fileName'] = file_name
            image_url_info['url']      = detail_image_url

            return image_url_info

        except Exception as e:
            raise e

    def get_product_detail(self, product_id, db_connection) :

        """

        Filtering을 통한 상품 List와 Total Count를 Return 하는Business Layer(service) function

        Args:

            db_connection    : DATABASE Connection Instance

        Returns:
            mainCategoryId    : Main Category ID
            subCategoryId     : Sub Category ID
            sellYn            : 상품 판매여부 (Boolean)
            exhibitionYn      : 상품 진열여부 (Boolean)
            productName       : 상품이름
            simpleDescription : 상품 한 줄 설명
            detailInformation : 상품 상세 설명
            price             : 상품가격
            discountRate      : 상품 할인율
            discountStartDate : 할인 시작일
            discountEndDate   : 할인 종료일
            minSalesQuantity  : 최소판매 수량
            maxSalesQuantity  : 최대판매 수량
            image_url         : image URL List
            [
              {
                "image_medium": 중간 사이즈(medium) image URL
              }
            ]
            "optionQuantity"  : 옵션별 수량 List
            [
                {
                    "colorName"       : 색상 이름
                    "sizeName"        : 사이즈 이름
                    "productOptionNo" : Option Number(PK)
                    "quantity"        : 옵션별 재고 수량
                }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-05 (sincerity410@gmail.com) : 초기생성

        """

        product_detail = self.product_dao.select_product_detail(product_id, db_connection)
        product_image  = self.product_dao.select_product_image(product_id, db_connection)
        product_option = self.product_dao.select_product_option(product_id, db_connection)

        # detail, image URL, option 정보를 Dictionary 형태로 Return
        product_info = {**product_detail, **product_image, **product_option}

        return product_info

    def update_product(self,product_id, product_info, db_connection) :
        """

        상품등록 - Business Layer(service) function

        Args:
            product_info  : 로 받은 Parameter
                mainCategoryId    : Main Category ID
                subCategoryId     : Sub Category ID
                sellYn            : 상품 판매여부 (Boolean)
                exhibitionYn      : 상품 진열여부 (Boolean)
                productName       : 상품이름
                simpleDescription : 상품 한 줄 설명
                detailInformation : 상품 상세 설명
                price             : 상품가격
                discountRate      : 상품 할인율
                discountStartDate : 할인 시작일
                discountEndDate   : 할인 종료일
                minSalesQuantity  : 최소판매 수량
                maxSalesQuantity  : 최대판매 수량
                optionQuantity    : 옵션별 수량 List
                {
                    colorId  : 상품 색상 id
                    sizeId   : 상품 사이즈 id
                    quantity : 상품 재고수량
                }

            db_connection : DATABASE Connection Instance

        Returns :
            product_id : products Table의 PK

        Author :
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-07 (sincerity410@gmail.com) : 초기생성

        """

        # 기존 옵션 정보 변수 선언
        option_quantity = {}

        # DB와 업데이트 정보 비교를 위한 변수 받아오기
        option_quantity['optionQuantity'] = json.loads(product_info['optionQuantity'])

        # request의 상품 detail 정보를 위해 key-value 제거
        del product_info['optionQuantity']

        # DB에서의 상품 상세정보(product_details, product_options) 가져오기
        product_detail = self.product_dao.select_product_detail_to_compare(product_id, db_connection)
        product_option = self.product_dao.select_product_option_to_compare(product_id, db_connection)

        # 옵션의 변경 발생 -> 옵션정보 수정 및 옵션 선분관리
        if product_option != option_quantity :
            # 선분 관리할 시간 저장
            now = self.product_dao.select_now(db_connection)

            # 선분이 관리되는 상세 옵션 번호 가져오기
            option_detail_no = self.product_dao.select_product_option(product_id, db_connection)

            # 기존 옵션 상세정보의 선분을 닫아주기
            for option in option_detail_no['optionQuantity']:
                self.product_dao.close_option_detail(now, option['optionDetailNo'], db_connection)

            # 상품 옵션 별 produc_options, option_details, quantities 테이블 insert 수행
            for option in option_quantity['optionQuantity']:
                product_option_id  = self.product_dao.insert_product_option(product_id, db_connection)

                color_id           = self.product_dao.select_color_id(option, db_connection)
                size_id            = self.product_dao.select_size_id(option, db_connection)
                option['color_id'] = color_id
                option['size_id']  = size_id

                option_detail_id   = self.product_dao.insert_option_detail(
                    now,
                    product_option_id,
                    option,
                    db_connection
                )
                self.product_dao.insert_quantity(option_detail_id, option, db_connection)

        # product에 insert 한 id를 product_info에 포함 > 상세정보 insert query 실행
        if product_detail != product_info:
            product_info['now']        = now
            product_info['product_id'] = product_id
            self.product_dao.close_product_detail(now, product_id, db_connection)
            self.product_dao.insert_product_detail(product_info, db_connection)

        return None
