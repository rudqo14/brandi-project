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
            product_info  :
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
            2020-09-08 (sincerity410@gmail.com) : 스키마 수정에 따른 함수 수정

        """

        try:
            # 선분 관리할 현재 시간 product_info에 저장
            product_info['now'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # product에 insert 한 id를 product_info에 포함 > 상세정보(product_details) insert query 실행
            product_info['product_id'] = self.product_dao.insert_product(db_connection)
            self.product_dao.insert_product_detail(product_info, db_connection)

            # nested JSON 구조인 optionQuantity를 form-data request로 받아 JSON 변환
            options = json.loads(product_info['optionQuantity'])

            # 상품 옵션 별 produc_options, option_details, quantities 테이블 insert 수행 
            for option in options :

                # name으로 입력된 각 옵션의 id를 받아옴
                color_id = self.product_dao.select_color_id(option, db_connection)
                size_id  = self.product_dao.select_size_id(option, db_connection)

                # insert_product_option 함수 인자를 줄이기 위해 option 정보 별도 저장
                option['color_id'] = color_id
                option['size_id']  = size_id

                # 옵션 정보 저장
                product_option_id  = self.product_dao.insert_product_option(product_info, option, db_connection)

                # 옵션에 해당하는 수량 정보 저장
                self.product_dao.insert_quantity(product_info['now'], product_option_id, option, db_connection)

            # Image S3 Upload 및 RDB에 URL Link insert를 위해 product_id return
            return product_info['product_id']

        except Exception as e:
            raise e

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

        try:
            # DB connection으로 각 옵션 정보 Return 하는 함수 호출
            colors = self.product_dao.select_color_list(db_connection)
            sizes  = self.product_dao.select_size_list(db_connection)

            # 모든 옵션 정보 Return
            return {'color' : colors, 'size' : sizes}

        except Exception as e:
            raise e

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

        try:
            # DB connection으로 사이즈 정보 Return 하는 select_size_list 함수 호출
            main_categories = self.product_dao.select_main_category_list(db_connection)

            # 모든 Main Category 정보 Return
            return main_categories

        except Exception as e:
            raise e

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

        try:
            # DB connection으로 사이즈 정보 Return 하는 select_size_list 함수 호출
            sub_categories = self.product_dao.select_sub_category_list(main_cetegory_id, db_connection)

            # 모든 Main Category 정보 Return
            return sub_categories

        except Exception as e:
            raise e

    def get_product_details(self, product_id, db_connection):

        """

        상품 상세정보 > 이미지들

        Args:
            product_id : 상품 고유의 id(pk)
            db_connection : 연결된 db 객체

        Returns:
            해당 상품의 이미지들

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-08-27 (minho.lee0716@gmail.com) : 초기 생성
            2020-08-30 (minho.lee0716@gmail.com) : 이미지 리스트를 details에 추가.
            2020-08-31 (minho.lee0716@gmail.com) : 상품 옵션들을 details에 추가.
            2020-09-01 (minho.lee0716@gmail.com) : 상품 옵션들중 색상만 주는걸로 변경.
            2020-09-01 (minho.lee0716@gmail.com) : 이미지나 색상이 없을 경우 빈 배열을 리턴하도록 수정.

        """

        # 해당 상품의 아이디를 받아 상세정보들을 가져옴.
        # 상세정보중 이미지들과 옵션들은 따로 가져와서 details에 추가.
        details = self.product_dao.select_product_details(product_id, db_connection)
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

        try:
            # page 값으로 offset 정보 획득
            filter_info['offset'] = filter_info['page'] * filter_info['limit'] - filter_info['limit']

            # DB connection으로 (상품 List & Total Count) Return 하는 select_registered_product_list 함수 호출
            product_list = self.product_dao.select_registered_product_list(filter_info, db_connection)

            return product_list

        except Exception as e:
            raise e

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
            product_id    : products Table PK
            db_connection : DATABASE Connection Instance

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

        try:
            # product_id(products Table PK) 기준으로 상품 상세, 이미지, 옵션에 대한
            product_detail = self.product_dao.select_product_detail(product_id, db_connection)
            product_image  = self.product_dao.select_product_image(product_id, db_connection)
            product_option = self.product_dao.select_product_option(product_id, db_connection)

            # detail, image URL, option 정보를 Dictionary 형태로 Return
            product_info = {**product_detail, **product_image, **product_option}

            return product_info

        except Exception as e:
            raise e

    def update_product(self, product_id, product_info, db_connection) :
        """

        상품 등록 >  상품 수정 - Business Layer(service) function

        Args:
            product_id    : products Table PK
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
            None

        Author :
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-07 (sincerity410@gmail.com) : 초기생성

        """
        try:
            # 기존 옵션 정보 변수 선언
            option_quantity = {}

            # DB와 업데이트 정보 비교를 위한 변수 받아오기
            option_quantity = json.loads(product_info['optionQuantity'])

            # request의 상품 detail 정보를 위해 key-value 제거
            del product_info['optionQuantity']

            # 비교를 위한 DB에서의 상품 상세정보(product_details, product_options) 가져오기
            product_detail = self.product_dao.select_product_detail_to_compare(product_id, db_connection)
            product_option = self.product_dao.select_product_option_to_compare(product_id, db_connection)

            # 선분 관리할 시간 생성
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 옵션의 변경 발생 -> 옵션정보 수정 및 옵션 삭제(재고수량(quantities Table) 포함)
            if product_option['optionQuantity'] != option_quantity :

                # request에만 존재하는 옵션을 저장
                request_only_option = option_quantity

                # DB의 상품옵션(product_options)에 대해 for Loop
                for db_option in product_option['optionQuantity']:

                    # request에는 없고 DB에만 있는 상품옵션(product_option) 체크를 위한 Bool 변수
                    is_option_db = False

                    # request의 상품옵션(product_options)에 대해 for Loop
                    for request_option in option_quantity:

                        # option은 동일, 수량만 변경된 경우
                        if request_option['color'] == db_option['color'] and request_option['size'] == db_option['size'] and request_option['quantity'] != db_option['quantity']:

                            # name으로 입력된 각 옵션의 id를 받아옴
                            color_id = self.product_dao.select_color_id(request_option, db_connection)
                            size_id  = self.product_dao.select_size_id(request_option, db_connection)

                            # insert_product_option 함수 인자를 줄이기 위해 option 정보 별도 저장
                            request_option['color_id'] = color_id
                            request_option['size_id']  = size_id

                            # 상품옵션 정보 Return
                            product_option_id = self.product_dao.select_product_option_number(product_id, request_option, db_connection)

                            # 기존 수량 정보(quantities 테이블) 선분이력 close
                            self.product_dao.close_quantity(now, product_option_id, db_connection)

                            # 옵션에 해당하는 수량 정보 저장(선분 생성)
                            self.product_dao.insert_quantity(now, product_option_id, request_option, db_connection)

                            # DB에도 동일한 option 존재 체크
                            is_option_db = True

                            # DB, request 모두 존재하는 옵션인 경우 제거
                            request_only_option.remove(request_option)

                            break

                        # request에는 없고, DB에 남은 옵션을 체크
                        if request_option['color'] == db_option['color'] and request_option['size'] == db_option['size']:

                            # DB에도 동일한 option 존재 체크
                            is_option_db = True

                            # DB, request 모두 존재하는 옵션인 경우 제거
                            request_only_option.remove(request_option)

                            break

                    # request(수정사항)에 새로 추가된 상품옵션(product_options) DB 상품옵션 soft delete
                    if not is_option_db:

                        # name으로 입력된 각 옵션의 id를 받아옴
                        color_id = self.product_dao.select_color_id(db_option, db_connection)
                        size_id  = self.product_dao.select_size_id(db_option, db_connection)

                        # insert_product_option 함수 인자를 줄이기 위해 option 정보 별도 저장
                        db_option['color_id'] = color_id
                        db_option['size_id']  = size_id

                        # 상품 옵션 삭제 처리를 위해 product option number select
                        product_option_id = self.product_dao.select_product_option_number(product_id, db_option, db_connection)

                        # request(수정사항)에 새로 추가된 상품옵션(product_options) DB 상품옵션 soft delete 실행
                        self.product_dao.delete_product_option(now, product_option_id, db_connection)

                # request에만 존재하는 option 정보 product_options 테이블에 insert
                for option in request_only_option:

                    # name으로 입력된 각 옵션의 id를 받아옴
                    color_id = self.product_dao.select_color_id(option, db_connection)
                    size_id  = self.product_dao.select_size_id(option, db_connection)

                    # insert_product_option 함수 인자를 줄이기 위해 option 정보 별도 저장
                    option['color_id'] = color_id
                    option['size_id']  = size_id

                    # product_id 설정
                    product_info['product_id'] = product_id

                    # 옵션 정보 저장
                    product_option_id = self.product_dao.insert_product_option(product_info, option, db_connection)

                    # 옵션에 해당하는 수량 정보 저장
                    self.product_dao.insert_quantity(now, product_option_id, option, db_connection)

            # 상품 상세 정보가 request(form-data)와 DB가 다른 경우
            if product_detail != product_info:

                # 기존 선분은 close 신규 선분은 start 되는 datatime 선언
                product_info['now'] = now

                # 새로 생성될 product_detail의 product_id 
                product_info['product_id'] = product_id

                # 기존 product_details row의 선분 close
                self.product_dao.close_product_detail(now, product_id, db_connection)

                # product_detail 테이블의 선분 신규 생성
                self.product_dao.insert_product_detail(product_info, db_connection)

            return None

        except Exception as e:
            raise e

    def update_product_image(self, images, product_id, s3_connection, db_connection):

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
            2020-09-09 (sincerity410@gmail.com) : 초기생성

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

            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.product_dao.close_product_image(now, product_id, db_connection)
            self.product_dao.delete_image(product_id, db_connection)

            # 사진크기 별 product_image(최대 5개)에 대해 image URL insert & product_images(매핑테이블) insert
            for product_image_no, image_url in resized_image.items() :
                image_no = self.product_dao.insert_image(image_url, db_connection)
                self.product_dao.insert_product_image(product_id, image_no, product_image_no, db_connection)

            return None

        except Exception as e:
            raise e
