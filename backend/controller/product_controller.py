from flask      import (
    request,
    Blueprint,
    jsonify,
)

from connection              import get_connection
from service.product_service import ProductService

class AdminProductView:
    # 'admin/'의 end point에 대한 처리
    product_app = Blueprint('product_app', __name__, url_prefix='/admin')

    @product_app.route('product', methods=['POST'])
    def product_register():
        """
        상품등록 엔드포인트
        [POST] http://ip:5000/admin/product

        request.body:
            mainCategoryId    : Main Category ID
            subCategoryId     : Sub Category ID
            sellYn            : 상품 판매여부 (Boolean)
            exhibitionYn      : 상품 진열여부 (Boolean)
            productName       : 상품이름
            simpleDescription : 상품 한 줄 설명
            detailInformation : 상품 상세 설명
            price             : 상품가격
            productImage      : 상품이미지(List)
            [
                {
                    imageUrl : 상품이미지 URL
                }
            ]
            discountRate      : 상품 할인율
            discountStartDate : 할인 시작일
            discountEndDate   : 할인 종료일
            minSalesQuantity  : 최소판매 수량
            maxSalesQuantity  : 최대판매 수량

        Returns:
            200 : SUCCESS, 상품등록 완료
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-25 (sincerity410@gmail.com) : 초기생성
        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:
                product_info          = request.json
                product_service       = ProductService()
                product_create_result = product_service.create_product(product_info, db_connection)
                return product_create_result

        finally:
            if db_connection:
                db_connection.close()

def product_endpoint(product_service):
    service_product_app = Blueprint('service_product_app', __name__, url_prefix='/product')

    @service_product_app.route('', methods=['GET'])
    def product_list():

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:
                products = product_service.get_product_list(db_connection)

                return jsonify({'data':products}), 200

        except Exception as e:
            return jsonify({'message':e}), 400

        finally:
            if db_connection:
                db_connection.close()

    return service_product_app
