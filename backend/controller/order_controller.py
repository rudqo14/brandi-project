import datetime

from flask                      import (
    Blueprint,
    request,
    jsonify
)
from flask_request_validator    import (
    GET,
    PATH,
    Param,
    validate_params
)

from connection import get_connection
from utils      import DatetimeRule, catch_exception, login_required

def create_admin_order_endpoints(order_service):
    admin_order_app = Blueprint('admin_order_app', __name__, url_prefix='/admin/order')

    @admin_order_app.route('/orderCompletedList', methods=['GET'], endpoint='order_list')
    @catch_exception
    @validate_params(
        Param('fromDate', GET, int, required=False, rules=[DatetimeRule()]),
        Param('page', GET, int),
        Param('limit', GET, int),
        Param('sort', GET, bool, default=False, required=False),
        Param('orderId', GET, int, required=False),
        Param('orderDetailId', GET, int, required=False),
        Param('orderer', GET, str, required=False),
        Param('phoneNumber', GET, str, required=False),
        Param('productName', GET, str, required=False)
    )
    def order_list(*args):

        db_connection = None

        try:

            # db 연결
            db_connection = get_connection()

            # request의 filter 정보 저장
            filter_info = {
                'from_date'         : args[0],
                'page'              : args[1],
                'limit'             : args[2],
                # 정렬 조건 존재하는경우 : 주문일 오래된 순
                'sort'              : args[3],
                'order_id'          : args[4],
                'order_detail_id'   : args[5],
                'orderer'           : args[6],
                'phone_number'      : args[7],
                'product_name'      : args[8]
            }

            if db_connection:

                # filter 유효성 검사
                filters = order_service.check_filter_list(filter_info)

                if filters:

                    # filter 조건 정보에 해당하는 총 결제 완료 건수 조회
                    count = order_service.get_total_number(filters, db_connection)

                    if count:

                        # filter 정보를 전달하여 결제 완료 리스트 가져와서 result에 저장
                        result = order_service.get_order_list(filters, db_connection)

                        if result:

                            # 총 갯수와 result return
                            return jsonify({"total_number" : count['total_number'], "data" : result}), 200

                        # page에 해당하는 data 없을 시
                        return jsonify({"total_number" : count['total_number'], "data" : []}),200

                    # 존재하는 데이터 없음
                    return jsonify({"total_number" : 0, "data" : []}), 200

                # filter 조건 불충족
                return jsonify({"message" : "INVALID_FILTER"}), 401

            # db 연결이 없을 시
            return jsonify({"message" : "NO_DATABASE_CONNECTION"}), 500

        except ValueError as e:
            return jsonify({"message" : f"VALUE_ERROR_AS_{e}"}), 400

        #정의하지 않은 모든 error를 잡아줌
        #except Exception as e:
            #return jsonify({"message" : f'{e}'}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_order_app.route('/detail/<order_detail_id>', methods=['GET'], endpoint='get_order_detail')
    @catch_exception
    @validate_params(
        Param('order_detail_id', PATH, int)
    )
    def get_order_detail(*args):

        db_connection = None

        try:
            # db 연결
            db_connection = get_connection()

            if db_connection:

                # order_detail_id에 해당하는 주문 상세정보를 가져옴
                result = order_service.get_order_detail({"order_detail_id" : args[0]}, db_connection)

                if result:
                    return jsonify({"data" : result}), 200

                # parameter로 들어온 주문 상세정보에 해당하는 data가 없을 때
                return jsonify({"data" : []}), 200

        # 정의하지 않은 모든 에러를 잡아줌
        except Exception as e:
            return jsonify({"message" : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    return admin_order_app

def create_service_order_endpoints(order_service):
    service_order_app = Blueprint('service_order_app', __name__, url_prefix='/order')

    @service_order_app.route('/checkout', methods=['GET'])
    #@login_required
    # 테스트를 하기위한 임의의 유저 id를 지정
    def product_info_to_purchase(user_no=4):

        """

        [ 서비스 > 구매할 상품 정보 ] 엔드포인트
        [GET] http://ip:5000/order/checkout?product_id=1&color_id=1&size_id=1&quantity=100

        Args:
            header:
                Authorization : access_token (여기서 user_no를 가져옴)

            Query Parameter:
                product_id  : 구매할 상품의 ID(번호)
                color_id    : 구매할 상품의 색상
                size_id     : 구매할 상품의 사이즈
                quantity    : 구매할 상품의 개수

        Returns:
            200 : data, {
                    "additional_address": "서울 어딘가",
                    "address": "서울특별시",
                    "color_name": "화이트",
                    "discount_rate": 30,
                    "image_small": "https://weplash.s3.ap-northeast-2.amazonaws.com/17993567_1594029656_image5_L.jpg",
                    "name": "선분이력테스트 (요즘대세/여유핏) 카라 반크롭 반팔티(4color)_버튼나인 - 버튼나인",
                    "orderer_email": "rudqo@rudqo.com",
                    "orderer_name": "김경배",
                    "phone_number": "01033334444",
                    "price": 11250.0,
                    "product_id": 1,
                    "quantity": "3",
                    "receiver": "김경배수령",
                    "size_name": "M",
                    "zip_code": "15279"
                  }
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-08-31 (minho.lee0716@gmail.com) : 초기생성
            2020-09-02 (minho.lee0716@gmail.com) : 메소드 변경 POST > GET

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            # DB에 연결이 됐다면
            if db_connection:

                # Query Parameter로 들어온 정보를 product_info에 담기.
                product_info = request.args
                # 잘못 들어왔을 때 예외처리하기
                #print(product_info)

                # 상세페이지에서 옵션을 선택 후, 구매하기 클릭시 상품 구매정보를 purchase_info에 담기
                purchase_info = order_service.get_product_info_to_purchase(product_info, user_no, db_connection)

                # 필요없는 정보라 삭제했습니다.
                #del purchase_info['discount_rate']
                #del purchase_info['price']

                purchase_info['quantity'] = product_info['quantity']

                return jsonify({'data' : purchase_info}), 200

            # DB에 연결이 되지 않았을 경우, DB에 연결되지 않았다는 에러메시지를 보내줍니다.
            return jsonify({'message' : 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message' : e}), 400

        finally:
            if db_connection:
                db_connection.close()

    return service_order_app
