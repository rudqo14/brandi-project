class OrderDao:

    def get_ordercompleted_list(self, db_connection):
        """
        결제 완료 리스트 표출

        Args:
            db_connection : 연결된 db 객체

        Returns:
            결제 완료 리스트

        Author:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-24 (tnwjd060124@gmail.com) : 초기 생성

        """

        cursor = db_connection.cursor()

        select_list = """
        SELECT
            P3.start_time AS order_time,
            P1.order_no,
            P2.order_product_no AS order_detail_no,
            P6.name AS product_name,
            P4.name AS size,
            P5.name AS color,
            P6.price,
            P2.quantity,
            P7.receiver,
            P7.phone_number,
            P9.name AS order_status

        FROM
            orders AS P1

        INNER JOIN order_product AS P2
        ON P1.order_no = P2.order_id

        INNER JOIN orders_details AS P3
        ON P1.order_no = P3.order_id
        AND P3.order_status_id=1

        INNER JOIN product_options AS P8
        ON P2.product_option_id = P8.product_option_no

        INNER JOIN sizes AS P4
        ON P8.size_id = P4.size_no

        INNER JOIN colors AS P5
        ON P8.color_id = P5.color_no

        INNER JOIN user_shipping_details AS P7
        ON P3.user_shipping_id = P7.user_shipping_detail_no

        INNER JOIN product_details AS P6
        ON P8.product_id = P6.product_id

        INNER JOIN order_status AS P9
        ON P3.order_status_id = P9.order_status_no
        """

        cursor.execute(select_list)
        orders = cursor.fetchall()

        return orders
