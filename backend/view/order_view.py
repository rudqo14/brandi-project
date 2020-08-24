from flask import Blueprint, request, jsonify

from connection import get_connection

def create_admin_order_endpoints(order_service):
    admin_order_app = Blueprint('admin_order_app', __name__, url_prefix='/admin/order')

    @admin_order_app.route('/orderCompletedList', methods=['GET'])
    def order_list():
        try:
            db_connection = get_connection()

            if db_connection:
                orders = order_service.get_order_list(db_connection)

                return jsonify({"data" : orders}), 200

        finally:
            if db_connection:
                db_connection.close()

    return admin_order_app
