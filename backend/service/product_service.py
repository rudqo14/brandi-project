import json
from PIL import Image

from utils import ResizeImage

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
                maxSalesQuantity  : 최대판매 수량TypeError: sequence item 0: expected str instance, dict found
                image_url         : 상품이미지(Dict)
                    {
                        'product_image_(No.)' : {
                            'product_image_L' : Large 사이즈 url,
                            'product_image_M' : Medium 사이즈 url,
                            'product_image_S' : Small 사이즈 url
                        }
                    }
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
            2020-08-25 (sincerity410@gmail.com) : 초기생성
            2020-08-26 (sincerity410@gmail.com) : controller, service, model role 재정의에 따른 함수수정
            2020-08-28 (sincerity410@gmail.com) : images, product_images insert 수행
            2020-08-30 (sincerity410@gmail.com) : option 별 재고수량 관련 테이블(product_options, option_details,
                                                  quantities) insert 수행

        """

        # product에 insert 한 id를 product_info에 포함 > 상세정보 insert query 실행
        product_info['product_id'] = self.product_dao.insert_product(db_connection)
        self.product_dao.insert_product_detail(product_info, db_connection)

        # 사진크기 별 product_image(최대 5개)에 대해 image URL insert & product_images(매핑테이블) insert
        for product_image_no, image_url in product_info['image_url'].items() :
            image_no = self.product_dao.insert_image(image_url, db_connection)
            self.product_dao.insert_product_image(product_info['product_id'], image_no, product_image_no, db_connection)

        # nested JSON 구조인 optionQuantity를 form-data로 받아 JSON 변환
        options = json.loads(product_info['optionQuantity'][0])

        # 상품 옵션 별 produc_options, option_details, quantities 테이블 insert 수행 
        for option in options :
            product_option_id = self.product_dao.insert_product_option(product_info['product_id'], db_connection)
            option_detail_id  = self.product_dao.insert_option_detail(product_option_id, option, db_connection)
            self.product_dao.insert_quantity(option_detail_id, option, db_connection)

        return None

    def get_product_list(self, db_connection):

        """

        브랜디 서비스 페이지 > 상품 전체 리스트

        Args:
            연결된 db 객체

        Returns:
            상품 전체 리스트

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-08-25 (minho.lee0716@gmail.com) : 초기 생성

        """

        # 상품의 기준은 진열여부=True, 판매여부=True
        products = self.product_dao.select_product_list(db_connection)

        # 모든 상품을 리턴
        return products

    def upload_product_image(self, images, s3_connection):

        """

        상품 이미지 등록 - Business Layer(service) function

        Args:
            images        : File Request(List)
                [
                    { 'product_image_<int>' : <FileStorage: {filename} ({content_type})>}
                ]
            s3_connection : S3 Connection Instance

        Returns:
            Image URL List:
            {
                'product_image_(No.)' : {
                    'product_image_L' : Large 사이즈 url,
                    'product_image_M' : Medium 사이즈 url,
                    'product_image_S' : Small 사이즈 url
                }
            }

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-27 (sincerity410@gmail.com) : 초기생성

        """

        # product image
        product_images = {}

        try:
            for idx in range(1,6):

                # 대표사진 미등록 시 예외처리
                if images.get(f'product_image_1', None) == None :
                    raise Exception('THUMBNAIL_IMAGE_IS_REQUIRED')

                # 상품사진 미정렬 시 예외처리
                if idx > 1  :
                    if (images.get(f'product_image_{idx}', None) != None) and (images.get(f'product_image_{idx-1}', None) == None) :
                        raise Exception('IMAGE_CAN_ONLY_REGISTER_IN_ORDER')

                # 상품사진 있는 경우 product_images Dictionary에 저장
                if images.get(f'product_image_{idx}', None) != None :
                    product_images[images[f'product_image_{idx}'].name] = images.get(f'product_image_{idx}', None)

                    # 파일이 Image가 아닌 경우 Exception 발생
                    image         = Image.open(product_images[f'product_image_{idx}'])
                    width, height = image.size

                    # 사이즈가 너무 작은 경우 예외처리
                    if width < 640 or height < 720 :
                        raise Exception('IMAGE_SIZE_IS_TOO_SMALL')

            # 상품 이미지 받아오기 및 유효성 검사 이후 S3 upload
            resizing = ResizeImage(product_images, s3_connection)
            return resizing()

        except Exception as e:
            raise e

    def get_color_list(self, db_connection) :

        """

        색상 목록을 Return 하는Business Layer(service) function

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            "data": [
                {
                    "color_no" : {color_no} ,
                    "name"     : "{color_nam}"
                }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성

        """

        # DB connection으로 사이즈 정보 Return 하는 select_size_list 함수 호출
        colors = self.product_dao.select_color_list(db_connection)

        # 모든 색상 정보 Return
        return colors

    def get_size_list(self, db_connection) :

        """

        사이즈 목록을 Return 하는Business Layer(service) function

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            "data": [
                {
                    "size_no" : {size_no},
                    "name"    : "{size_name}"
                }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성

        """

        # DB connection으로 사이즈 정보 Return 하는 select_size_list 함수 호출
        sizes = self.product_dao.select_size_list(db_connection)

        # 모든 사이즈 정보 Return
        return sizes
