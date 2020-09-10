from flask                      import (
    Blueprint,
    request,
    jsonify
)
from flask_request_validator    import (
    GET,
    PATH,
    Param,
    JSON,
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

    return admin_order_app

def create_service_order_endpoints(order_service):
    service_order_app = Blueprint('service_order_app', __name__, url_prefix='/order')

    @service_order_app.route('/checkout', methods=['GET'], endpoint="product_info_to_purchase")
    @catch_exception
    @validate_params(
        Param('product_id', GET, int),
        Param('color_id', GET, int),
        Param('size_id', GET, int),
        Param('quantity', GET, int),
    )
    @login_required
    def product_info_to_purchase(user_info, *args):

        """

        [ 서비스 > 구매할 상품 정보 ] 엔드포인트
        [GET] http://ip:5000/order/checkout?product_id=1&color_id=1&size_id=1&quantity=100

        Args:
            header:
                Authorization(user_info) : {'user_no' : 해당 유저의 id}

            Params:
                product_id : 구매할 상품의 ID(번호)
                color_id   : 구매할 상품의 색상
                size_id    : 구매할 상품의 사이즈
                quantity   : 구매할 상품의 개수

        Returns:
            200 : data, {
                    "additional_address" : "서울 어딘가",
                    "address"            : "서울특별시",
                    "color_id"           : 2,
                    "color_name"         : "화이트",
                    "discount_rate"      : 30,
                    "image_small"        : "작은 사진 이미지 URL주소",
                    "name"               : "상품 이름",
                    "orderer_email"      : "rudqo@rudqo.com",
                    "orderer_name"       : "김경배",
                    "phone_number"       : "01033334444",
                    "price"              : 11250.0,
                    "product_id"         : 1,
                    "quantity"           : "3",
                    "receiver"           : "김경배수령",
                    "size_id"            : 4,
                    "size_name"          : "M",
                    "zip_code"           : "15279"
                  }
            400 : VALIDATION_ERROR
            400 : THIS_PRODUCT_DOES_NOT_EXISTS
            400 : UNAUTHORIZED
            400 : The maximum/minimum number of products that can be purchased is 'quantity' or more/less.
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-08-31 (minho.lee0716@gmail.com) : 초기생성
            2020-09-02 (minho.lee0716@gmail.com) : 메소드 변경 POST > GET
            2020-09-03 (minho.lee0716@gmail.com) : 예외 처리
                Params가 들어오지 않았을 경우 + Params의 키 값이 잘못 들어왔을 경우
            2020-09-08 (minho.lee0716@gmail.com) : 프론트와 API를 맞춰보기 위해 Token관련 데코레이터 사용.
            2020-09-09 (minho.lee0716@gmail.com) : flask_request_validator를 이용해 Params의 유효성 검사.
            2020-09-10 (minho.lee0716@gmail.com) : 추가
                해당 상품의 구매 가능한 최소, 최대 수량을 가져와 받아온 수량을 확인하여
                최소 구매 수량보다 적게 샀을 경우와 최대 구매 수량보다 많이 샀을 경우에 대한 에러처리를 하였습니다.

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            # DB에 연결이 잘 되었다면,
            if db_connection:

                # 유효성 검사를 통과한 Params로 들어온 정보를 product_info에 담습니다.
                product_info = {
                    'product_id' : args[0],
                    'color_id'   : args[1],
                    'size_id'    : args[2],
                    'quantity'   : args[3]
                }

                # 받아온 user_info객체에서 유저의 id를 가져옵니다.
                user_no = user_info['user_no']

                # 해당 유저의 정보가 올바른 유저인지 검사해줍니다.
                user_existence = order_service.check_user_existence(user_no, db_connection)

                # 해당 유저의 정보가 없다면,
                if user_existence is None:

                    # UNAUTHORIZED 에러 메세지를 보내줍니다.
                    return jsonify({'message' : 'UNAUTHORIZED'}), 401

                # 해당 상품의 구매가능한 최소수량과 최대수량의 개수를 가져옵니다.
                product_quantity_range = order_service.get_product_quantity_range(product_info, db_connection)

                # 가져온 최소, 최대 구매 가능한 상품의 수량을 각 변수에 담아줍니다.
                min_q = product_quantity_range['min_sales_quantity']
                max_q = product_quantity_range['max_sales_quantity']

                # 구매하려고 하는 상품의 수량이 최소 구매 가능한 수량보다 작을 때
                if product_info['quantity'] < min_q:
                    return jsonify({'message' : f"The minimum number of products that can be purchased is {min_q} or more."}), 400

                # 구매하려고 하는 상품의 수량이 최대 구매 가능한 수량보다 많을 때
                if product_info['quantity'] > max_q:
                    return jsonify({'message' : f"The maximum number of products that can be purchased is {max_q} or less."}), 400

                # 상세페이지에서 옵션을 선택 후, 구매하기 클릭시 상품 구매정보를 purchase_info에 담기
                # 로그인이 되어있는 사용자만이 구매를 할 수 있기 때문에 user_no도 넘겨줍니다.
                purchase_info = order_service.get_product_info_to_purchase(product_info, user_no, db_connection)

                # 구매 정보에 수량을 추가해 줍니다.
                purchase_info['quantity'] = product_info['quantity']

                return jsonify({'data' : purchase_info}), 200

            # DB에 연결이 되지 않았을 경우, DB에 연결되지 않았다는 에러메시지를 보내줍니다.
            return jsonify({'message' : 'NO_DATABASE_CONNECTION'}), 500

        # 정의하지 않은 모든 에러를 잡아줍니다.
        except Exception as e:
            return jsonify({'message' : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    @service_order_app.route('/completed', methods=['POST'], endpoint="order_completed")
    @catch_exception
    @validate_params(
        Param('product_id', JSON, int),
        Param('color_id', JSON, int),
        Param('size_id', JSON, int),
        Param('quantity', JSON, int),
        Param('total_price', JSON, int),
        Param('receiver', JSON, str),
        Param('phone_number', JSON, str),
        Param('zip_code', JSON, str),
        Param('address', JSON, str),
        Param('additional_address', JSON, str),
        Param('delivery_request', JSON, str),
    )
    @login_required
    def order_completed(user_info, *args):

        """

        [ 서비스 > 결제 완료(상품 주문 완료) ] 엔드포인트
        [POST] http://ip:5000/order/completed

        Args:
            header:
                Authorization(user_info) : {'user_no' : 해당 유저의 id}

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
            400 : The maximum/minimum number of products that can be purchased is 'quantity' or more/less.
            400 : The number of products available for purchase has been exceeded.
            400 : Total price is incorrect.
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-09-03 (minho.lee0716@gmail.com) : 초기생성
            2020-09-08 (minho.lee0716@gmail.com) : 프론트와 API를 맞춰보기 위해 Token관련 데코레이터 사용.
            2020-09-09 (minho.lee0716@gmail.com) : flask_request_validator를 이용해 Body의 유효성 검사.
            2020-09-10 (minho.lee0716@gmail.com) : 추가
                해당 상품의 구매 가능한 최소, 최대 수량을 가져와 받아온 수량을 확인하여
                최소 구매 수량보다 적게 샀을 경우와 최대 구매 수량보다 많이 샀을 경우에 대한 에러처리를 하였습니다.
            2020-09-10 (minho.lee0716@gmail.com) : 추가
                프론트에서 받아온 구매할 상품에 대한 총 가격에이 DB에 있는 상품의 정보를 이용한 총 가격과 일치하는지
                검사를 하였고, 일치해야만 주문이 진행되게 하였습니다.

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            # DB에 연결이 됐다면
            if db_connection:

                # 유효성 검사를 통과한 Body로 들어온 정보를 order_info에 담습니다.
                order_info = {
                    "product_id"         : args[0],
                    "color_id"           : args[1],
                    "size_id"            : args[2],
                    "quantity"           : args[3],
                    "total_price"        : args[4],
                    "receiver"           : args[5],
                    "phone_number"       : args[6],
                    "zip_code"           : args[7],
                    "address"            : args[8],
                    "additional_address" : args[9],
                    "delivery_request"   : args[10]
                }

                # 데코레이터에서 받은 user_info객체에서 user_no을 가져옵니다.
                user_no = user_info['user_no']

                # 해당 유저의 정보가 올바른 유저인지 검사해줍니다.
                user_existence = order_service.check_user_existence(user_no, db_connection)

                # 해당 유저의 정보가 없다면,
                if user_existence is None:

                    # UNAUTHORIZED 에러 메세지를 보내줍니다.
                    return jsonify({'message' : 'UNAUTHORIZED'}), 401

                # user_no의 값을 쓰기 편하도록 order_info에 넣어줍니다.
                order_info['user_no'] = user_no

                # 해당 상품의 구매가능한 최소수량과 최대수량의 개수를 가져와 product_quantity_range라는 변수에 담아줍니다.
                product_quantity_range = order_service.get_product_quantity_range(order_info, db_connection)

                # 가져온 최소, 최대 구매 가능한 상품의 수량을 각 변수에 담아줍니다.
                min_q = product_quantity_range['min_sales_quantity']
                max_q = product_quantity_range['max_sales_quantity']

                # 구매하려고 하는 상품의 수량이 최소 구매 가능한 수량보다 적을 때
                if order_info['quantity'] < min_q:

                    # 최소한 n개 이상의 수량을 구매해야 한다고 에러 메세지를 보내줍니다.
                    return jsonify({'message' : f"The minimum number of products that can be purchased is {min_q} or more."}), 400

                # 구매하려고 하는 상품의 수량이 최대 구매 가능한 수량보다 많을 때
                if order_info['quantity'] > max_q:

                    # 최대 n개 이하의 수량을 구매해야 한다고 에러 메세지를 보내줍니다.
                    return jsonify({'message' : f"The maximum number of products that can be purchased is {max_q} or less."}), 400

                # 상품을 주문하기 전, 현재 선택한 옵션의 상품 재고를 가져오는 메소드를 실행 후, 변수에 담아줍니다.
                current_quantity = order_service.get_current_quantity(order_info, db_connection)

                # 만약 사용자가 구매하려는 상품의 개수가 현재 재고보다 많다면,
                if order_info['quantity'] > current_quantity['current_quantity']:

                    # 구매 가능한 상품의 수가 초과되었다고 에러를 보내줍니다.
                    return jsonify({'message' : 'The number of products available for purchase has been exceeded.'}), 400

                # 구매하고자 하는 수량에 문제가 없다면, 유저가 구매하고자 하는 수량에 대해 총 가격에 대한 검사를 해줍니다.
                # 먼저 주문 정보를 알려준 후, 총 가격을 계산해주는 메소드를 실행하여 total_price라는 변수에 넣어줍니다.
                total_price = order_service.check_total_price(order_info, db_connection)

                # 만약 프론트에서 계산한 총 가격과, DB에서 계산한 총 가격이 다르다면,
                if order_info['total_price'] != total_price:

                    # 결제를 진행하지 않고 에러 메세지를 보내줍니다.
                    return jsonify({'message' : 'Total price is incorrect.'}), 400

                # 프론트에서 계산한 총 가격이 문제가 없다면 결제를 이어서 진행합니다.
                # 만약 사용자가 구매하려는 상품의 개수가 현재 재고와 작거나 같다면 이어서 결제를 진행합니다.
                # 구매하기전, 해당 유저의 배송지 정보를 추가 또는 변경해주는 메소드를 호출합니다.
                order_service.modify_user_shipping_details(order_info, db_connection)

                # order의 정보를 인자로 넘겨 주문이력을 생성하는 메소드를 호출해 줍니다.
                order_service.create_order_completed(order_info, db_connection)

                # 마지막으로 상품결제를 하고, 한번 더 검사를 해줍니다.
                # DB에 현재 옵션에 대한 재고가 0보다 작다면,
                if order_service.get_current_quantity(order_info, db_connection)['current_quantity'] < 0:

                    # 똑같이 구매 가능한 상품의 수가 초과되었다고 에러를 보내줍니다.
                    return jsonify({'message' : 'The number of products available for purchase has been exceeded.'}), 400

                # 만약 재고가 0개 이상이라면 DB에 정상적으로 저장을 해줍니다.
                db_connection.commit()

                return jsonify({'message' : 'SUCCESS'}), 200

            # DB에 연결이 되지 않았을 경우, DB에 연결되지 않았다는 에러메시지를 보내줍니다.
            return jsonify({'message' : 'NO_DATABASE_CONNECTION'}), 500

        # 에러가 발생한 경우,
        except Exception as e:

            # DB를 원래대로 되돌립니다.
            db_connection.rollback()
            return jsonify({"message" : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    return service_order_app
