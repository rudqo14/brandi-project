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
        Param('productName', GET, str, required=False),
        Param('toDate', GET, int, required=False, rules=[DatetimeRule()])
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
                'product_name'      : args[8],
                'to_date'           : args[9]
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
        except Exception as e:
            return jsonify({"message" : f'{e}'}), 400

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

    @admin_order_app.route('/delete/<order_id>', methods=['DELETE'], endpoint='delete_order')
    @catch_exception
    @validate_params(
        Param('order_id', PATH, int)
    )
    def delete_order(order_id):

        db_connection = None

        try:

            # db 연결
            db_connection = get_connection()

            if db_connection:

                # 주문 취소 메소드 실행하기 위한 data
                order_data = {
                    "order_id" : order_id
                }

                # order_id 에 해당하는 주문완료 data가 있는지 확인 리턴값으로 order_detail_id 가 포함된 dictionary
                order = order_service.get_completed_order_detail(order_data, db_connection)

                # order_detail_id 가 None이 아닌경우
                if order['order_detail_id']:

                    # 주문 취소 메소드 실행 하기 위해 order_detail_id 설정
                    order_data = {**order_data, **order}

                    # 주문 완료 data가 있는 경우에만 취소하는 메소드 실행
                    result = order_service.delete_completed_order(order_data, db_connection)

                    if result:

                        return jsonify({"message" : "DELETE_SUCCESS"}), 200

                    # 주문취소 실패
                    db_connection.rollback()
                    return jsoinfy({"message" : "DELETE_FAIL"}), 400

                # order_id에 해당하는 주문완료 data가 없을 때
                return jsoinfy({"message" : "NO_ORDER_DATA"}), 401

        except Exception as e:
            db_connection.rollback()
            return jsoinfy({"message" : f"{e}"}), 400

        finally:

            if db_connection:
                db_connection.close()


    return admin_order_app

def create_service_order_endpoints(order_service):
    service_order_app = Blueprint('service_order_app', __name__, url_prefix='/order')

    @service_order_app.route('/checkout', methods=['GET'])
    @login_required
    def product_info_to_purchase(user_info):

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
            400 : QUERY_PARAMETER_DOES_NOT_EXISTS
            400 : KEY_ERROR_PRODUCT_ID
            400 : KEY_ERROR_COLOR_ID
            400 : KEY_ERROR_SIZE_ID
            400 : KEY_ERROR_QUANTITY
            400 : THIS_PRODUCT_DOES_NOT_EXISTS
            400 : UNAUTHORIZED
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-08-31 (minho.lee0716@gmail.com) : 초기생성
            2020-09-02 (minho.lee0716@gmail.com) : 메소드 변경 POST > GET
            2020-09-03 (minho.lee0716@gmail.com) : 예외 처리
                Params가 들어오지 않았을 경우 + Params의 키 값이 잘못 들어왔을 경우

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            # DB에 연결이 됐다면
            if db_connection:

                # 먼저 Query Parameter가 들어오지 않았을 경우의 에러조건입니다.
                if not request.args:
                    raise Exception('QUERY_PARAMETER_DOES_NOT_EXISTS')

                # Query Parameter로 들어온 정보를 product_info에 담습니다.
                product_info = request.args

                # Query Parameter로 들어온 키 값이 잘못된 경우의 에러조건입니다.
                if not 'product_id' in product_info.keys():
                    raise Exception('KEY_ERROR_PRODUCT_ID')

                if not 'color_id' in product_info.keys():
                    raise Exception('KEY_ERROR_COLOR_ID')

                if not 'size_id' in product_info.keys():
                    raise Exception('KEY_ERROR_SIZE_ID')

                if not 'quantity' in product_info.keys():
                    raise Exception('KEY_ERROR_QUANTITY')

                # 받아온 user_info객체에서 user_no를 가져옵니다.
                user_no = user_info['user_no']

                # 상세페이지에서 옵션을 선택 후, 구매하기 클릭시 상품 구매정보를 purchase_info에 담기
                # 로그인이 되어있는 사용자만이 구매를 할 수 있기 때문에 user_no도 넘겨줍니다.
                purchase_info = order_service.get_product_info_to_purchase(product_info, user_no, db_connection)

                # 구매 정보에 수량을 추가해 줍니다.
                purchase_info['quantity'] = product_info['quantity']

                return jsonify({'data' : purchase_info}), 200

            # DB에 연결이 되지 않았을 경우, DB에 연결되지 않았다는 에러메시지를 보내줍니다.
            return jsonify({'message' : 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message' : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    @service_order_app.route('/completed', methods=['POST'])
    @login_required
    def order_completed(user_info):

        """

        [ 서비스 > 상품 주문 완료(결제하기) ] 엔드포인트
        [POST] http://ip:5000/order/completed

        Args:
            header:
                Authorization : access_token (여기서 user_no를 가져옴)

            body:
                product_id         : 상품의 id
                color_id           : 색상의 id
                size_id            : 사이즈의 id
                quantity           : 수량
                total_price        : 총가격
                receiver           : 배송지 정보 - 수령인
                phone_number       : 배송지 정보 - 휴대폰 번호
                zip_code           : 배송지 정보 - 우편번호
                address            : 배송지 정보 - 주소
                additional_address : 배송지 정보 - 상세 주소
                delivery_request   : 배송지 정보 - 배송 요청 사항

        Returns:
            200 : message, SUCCESS
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-09-03 (minho.lee0716@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            # DB에 연결이 됐다면
            if db_connection:

                # Body로 들어온 정보를 order_info에 담기.
                order_info = request.json

                user_no = user_info['user_no']

                # 받아온 정보들로 주문하기
                order_service.create_order_completed(order_info, user_no, db_connection)

                db_connection.commit()

                return jsonify({'message' : 'ORDER_COMPLETED!!!'}), 200

            # DB에 연결이 되지 않았을 경우, DB에 연결되지 않았다는 에러메시지를 보내줍니다.
            return jsonify({'message' : 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            db_connection.rollback()
            return jsonify({"message" : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    return service_order_app
