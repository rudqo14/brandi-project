from flask import (
    request,
    Blueprint,
    jsonify,
)

from connection import get_connection
from utils      import ResizeImage

def create_admin_product_endpoints(product_service):

    # 'admin/product' end point prefix 설정
    admin_product_app = Blueprint('product_app', __name__, url_prefix='/admin/product')

    @admin_product_app.route('', methods=['POST'])
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
                product_create_result = product_service.create_product(product_info, db_connection)
                db_connection.commit()
                return product_create_result

        except Exception as e:
            return jsonify({"message" : f'{e}'}), 400

        finally:
            if db_connection:
                db_connection.close()


    # resizing 테스트
    @admin_product_app.route('/test', methods=['POST'])
    def test_image_resize():
        images = request.files
        resizing = ResizeImage(images)
        print(resizing())

        return jsonify({"data" : "resizing test"}), 200

    return admin_product_app

def service_product_endpoint(product_service):

    # '/product' end point prefix 설정
    service_product_app = Blueprint('service_product_app', __name__, url_prefix='/product')

    @service_product_app.route('', methods=['GET'])
    def product_list():

        """

        [ 서비스 > 상품 전체 리스트 ] 엔드포인트
        [GET] http://ip:5000/product

        Returns:
            200 : data, [ 서비스 > 상품 전체 리스트 ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-08-25 (minho.lee0716@gmail.com) : 초기생성
            2020-08-26 (minho.lee0716@gmail.com) : 수정
                엔드포인트를 찾아가지 못하는 문제 해결
            2020-08-27 (minho.lee0716@gmail.com) : 수정
                상품이 하나도 존재하지 않을 경우 빈 배열을 리턴

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            # DB에 연결이 잘 되었을 경우
            if db_connection:

                # 모든 상품을 products라는 변수에 가져와 담습니다.
                products = product_service.get_product_list(db_connection)

                # 상품이 1개라도 존재하지 않을 경우 json 리턴값이 null 인걸 확인하였고, 그럴 경우엔
                if not products:
                    # 빈 배열을 리턴해줍니다.
                    return jsonify({'data' : []}), 200

                # 상품이 1개 이상 존재할 경우, 모든 상품 리스트를 리턴해줍니다.
                return jsonify({'data' : products}), 200

            # DB에 연결이 되지 않았을 경우, DB에 연결되지 않았다는 에러메시지를 보내줍니다.
            return jsonify({'message' : 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message' : e}), 400

        finally:
            if db_connection:
                db_connection.close()

    @service_product_app.route('/<int:product_id>', methods=['GET'])
    def product_details(product_id):

        """

        [ 서비스 > 상품 상세정보 ] 엔드포인트
        [GET] http://ip:5000/product/product_id

        Returns:
            200 : data, [ 서비스 > 상품 상세정보 ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-08-27 (minho.lee0716@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()
            return jsonify({'data':product_id}), 200

        except Exception as e:
            return jsonify({'message' : e}), 400

        finally:
            if db_connection:
                db_connection.close()

    return service_product_app
