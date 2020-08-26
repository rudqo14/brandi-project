from PIL import Image

from flask import jsonify

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
                maxSalesQuantity  : 최대판매 수량
                image_url         : 상품이미지(Dict)
                    {
                        'product_image_(No.)' : {
                            'product_image_L' : Large 사이즈 url,
                            'product_image_M' : Medium 사이즈 url
                            'product_image_S' : Small 사이즈 url
                        }
                    }

            db_connection : DATABASE Connection Instance

        Returns :
            product_detail_id : 생성한 product_details row id

        Author :
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-25 (sincerity410@gmail.com) : 초기생성
            2020-08-26 (sincerity410@gmail.com) : controller, service, model role 재정의에 따른 함수수정
            2020-08-28 (sincerity410@gmail.com) : images, product_images insert 수행

        """

        # product에 insert 한 id를 product_info에 포함 > 상세정보 insert query 실행
        product_id                 = self.product_dao.insert_product(db_connection)
        product_info['product_id'] = product_id
        product_detail_id          = self.product_dao.insert_product_detail(product_info, db_connection)

        # 사진크기 별 product_image(최대 5개)에 대해 image URL insert & product_images(매핑테이블) insert
        for product_image_no, image_url in product_info['image_url'].items() :
            image_id = self.product_dao.insert_image(image_url, db_connection)
            self.product_dao.insert_product_image(product_id, image_id, product_image_no, db_connection)

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
            200: SUCCESS, Image URL

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

