class OrderService:

    def __init__(self, order_dao):
        self.order_dao = order_dao

    def get_order_list(self, db_connection):
        """
        결제 완료 리스트 표출 로직

        Args:
            연결된 db 객체

        Returns:
            결제 완료 리스트

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-24 (tnwjd060124@gmail.com) : 초기 생성
        """

        orders = self.order_dao.get_ordercompleted_list(db_connection)

        return orders
