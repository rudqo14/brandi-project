import datetime

from flask import Blueprint, request, jsonify

from connection import get_connection

def create_admin_order_endpoints(order_service):
    admin_order_app = Blueprint('admin_order_app', __name__, url_prefix='/admin/order')

    @admin_order_app.route('/orderCompletedList', methods=['GET'])
    def order_list():

        db_connection = None

        try:

            # db 연결
            db_connection = get_connection()

            # request의 filter 정보 저장
            filter_info = {
                'from_date'         : request.args.get('fromDate', default=None),
                'page'              : request.args.get('page', default=1),
                'limit'             : request.args.get('limit', default=50),
                # 정렬 조건 존재하는경우 : 주문일 오래된 순
                'sort'              : request.args.get('sort', default=False),
                'order_id'          : request.args.get('orderId', default=None),
                'order_detail_id'   : request.args.get('orderDetailId', default=None),
                'orderer'           : request.args.get('orderer', default=None),
                'phone_number'      : request.args.get('phoneNumber', default=None),
                'product_name'      : request.args.get('productName', default=None)
            }

            if db_connection:

                # filter 유효성 검사
                filters = order_service.check_filter_list(filter_info)

                if filters:

                    # filter 조건 정보에 해당하는 총 결제 완료 건수 조회
                    count = order_service.get_total_number(filters, db_connection)

                    # filter 정보를 전달하여 결제 완료 리스트 가져와서 result에 저장
                    result = order_service.get_order_list(filters, db_connection)

                    if result:

                        # 총 갯수와 result return
                        return jsonify({"total_number" : count['total_number'], "data" : result}), 200

                    # 존재하는 데이터 없음
                    return jsonify({"total_number" : 0, "data" : []}), 200

                # filter 조건 불충족
                return jsonify({"message" : "INVALID_FILTER"}), 401

            # db 연결이 없을 시
            return jsonify({"message" : "NO_DATABASE_CONNECTION"}), 500

        # 정의하지 않은 모든 error를 잡아줌
        except Exception as e:
            return jsonify({"message" : f'{e}'}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_order_app.route('/detail/<int:order_detail_id>', methods=['GET'])
    def get_order_detail(order_detail_id):

        db_connection = None

        try:
            # db 연결
            db_connection = get_connection()

            if db_connection:

                # order_detail_id에 해당하는 주문 상세정보를 가져옴
                result = order_service.get_order_detail({"order_detail_id" : order_detail_id}, db_connection)

                if result:
                    return jsonify({"data" : result}), 200

        # 정의하지 않은 모든 에러를 잡아줌
        except Exception as e:
            return jsonify({"message" : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    return admin_order_app
