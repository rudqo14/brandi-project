class OrderService:

    def __init__(self, order_dao):
        self.order_dao = order_dao

    def get_order_list(self, filter_info, db_connection):

        """

        결제 완료 리스트 표출 로직

        Args:
            filter_info : 필터 리스트
            db_connection : 연결된 db 객체

        Returns:
            결제 완료 리스트

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-24 (tnwjd060124@gmail.com) : 초기 생성

        """

        # 결제 완료 리스트 가져오는 메소드 실행
        orders = self.order_dao.get_ordercompleted_list(filter_info, db_connection)

        return orders

    def check_filter_list(self, filter_info):

        """

        filter의 유효성 체크

        Args:
            filter_info:
                page : 현재 페이지
                limit : 가져올 row 갯수
                from_date : 날짜 filter
                order_id : 주문_id
                order_detail_id : 주문 상세_id
                phone_number : 휴대폰번호
                orderer : 주문자명
                product_name : 상품명

        Returns:
            필터 리스트

            None : 조건 불충족 시

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-25 (tnwjd060124@gmail.com) : 초기 생성

        """

        # offset 설정
        filter_info['offset'] = (filter_info['page']*filter_info['limit']) - filter_info['limit']

        if not filter_info['from_date']:

            # filter에 날짜 정보가 없으면 검색 조건 정보 존재 확인
            if not( filter_info['order_id']
                    or filter_info['order_detail_id']
                    or filter_info['phone_number']
                    or filter_info['orderer']
                    or filter_info['product_name'] ):
                return None

        if filter_info['to_date']:
            filter_info['to_date'] += 1

        if filter_info['product_name']:
            filter_info['product_name'] = f"%{filter_info['product_name']}%"

        return filter_info

    def get_total_number(self, filters, db_connection):

        """

        총 결제 완료 건수 조회

        Args:
            filters : 필터 리스트
            db_connection : 연결된 db 객체

        Returns:
            총 결제 완료 건수

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-25 (tnwjd060124@gmail.com) : 초기 생성

        """

        # 총 결제 완료 건수 조회 메소드 실행
        total_number = self.order_dao.get_total_num(filters, db_connection)

        return total_number

    def get_order_detail(self, order_detail, db_connection):

        """

        주문 상세 정보 조회

        Args:
            order_detail : 주문 상세정보 id
            db_connection : 연결된 db 객체

        Returns:
            주문 상세 정보 detail

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-25 (tnwjd060124@gmail.com) : 초기 생성

        """

        # 주문 상세 정보 조회 메소드 실행
        order_detail = self.order_dao.get_detail(order_detail, db_connection)

        return order_detail

    def get_product_info_to_purchase(self, product_info, user_no, db_connection):

        """

        상품 상세정보에서 구매 클릭시 나오는 구매할 상품 정보, 주문자 정보, 배송지 정보를 리턴합니다.

        Args:
            product_info  : 구매할 상품에 대한 정보(product_id, color_id, size_id)
            user_no       : 토큰에서 받은 유저 id입니다.
            db_connection : 연결된 db 객체

        Returns:
            구매할 상품의 정보, 주문하려는 유저의 정보, 주문하려는 유저의 배송지 정보.

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-09-02 (minho.lee0716@gmail.com) : 초기 생성
            2020-09-03 (minho.lee0716@gmail.com) : 수정
                (구매하려는 상품의 정보 + 주문자의 정보 + 주문자의 배송지 정보)를 합쳤습니다.

        """

        # 셀러의 판매 상품(내가 고른 상품)에 대한 정보를 리턴해 줍니다.
        seller_product_info = self.order_dao.get_seller_product_info(product_info, db_connection)

        # 유저의 정보를 넘겨줌으로써 유저의 정보와 배송지 정보를 리턴해 줍니다.
        orderer_info = self.order_dao.get_orderer_info(user_no, db_connection)

        # 셀러 상품의 정보와 주문자의 정보, 주문자의 배송지 정보까지 한번에 리턴해 줍니다.
        return {**seller_product_info, **orderer_info}

    def create_order_completed(self, order_info, user_no, db_connection):

        """

        asdf

        Args:
            product_info  : 주문 관련에 관한 모든 정보입니다.
            user_no       : 토큰에서 받은 유저 id입니다.
            db_connection : 연결된 db 객체

        Returns:
            구매할 상품의 정보, 주문하려는 유저의 정보, 주문하려는 유저의 배송지 정보.

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-09-06 (minho.lee0716@gmail.com) : 초기 생성

        """

        # 유저의 id를 넘겨주고, orders 테이블에 insert후, 해당 order_no의 id(pk)를 가져옵니다.
        order_info['order_no'] = self.order_dao.insert_orders(user_no, db_connection)

        # orders_details테이블에 필요한 user_no의 정보를 order_info에 넣어줍니다.
        order_info['user_no'] = user_no

        # orders_details에 생성된 테이블의 id(pk)를 order_info에 넣어줍니다.
        order_info['order_detail_no']  = self.order_dao.insert_orders_details(order_info, db_connection)
        print('1')
        order_info['order_product_no'] = self.order_dao.insert_order_product(order_info, db_connection)
        print('2')
        order_info['quantity_no']      = self.order_dao.insert_quantities(order_info, db_connection)
        print('3')
        print(order_info)
        self.order_dao.update_quantities(order_info, db_connection)
        print('4')

        return None
