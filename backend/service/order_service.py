import math, datetime

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

        if not (filter_info['from_date'] or filter_info['to_date']):

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

        # dao 메소드 실행결과가 존재하는 경우에만 할인 가격 계산
        if order_detail:

            order_detail['sales_price'] = round((order_detail['original_price'] * (100 - order_detail['discount_rate'])) / 100, -1)

            return order_detail

        return None

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
            2020-09-03 (minho.lee0716@gmail.com) : 수정
                상품을 주문할 수 있게 프론트에게 option_detail_id를 리턴해 줍니다.

        """

        # 셀러의 판매 상품(내가 고른 상품)에 대한 정보를 리턴해 줍니다.
        seller_product_info = self.order_dao.get_seller_product_info(product_info, db_connection)

        # 할인된 가격 계산
        seller_product_info['sales_price'] = round(seller_product_info['original_price'] * (100 - seller_product_info['discount_rate'])/ 100, -1)

        # 유저의 정보를 넘겨줌으로써 유저의 정보와 배송지 정보를 리턴해 줍니다.
        orderer_info = self.order_dao.get_orderer_info(user_no, db_connection)

        # 셀러 상품의 정보와 주문자의 정보, 주문자의 배송지 정보까지 한번에 리턴해 줍니다.
        return {**seller_product_info, **orderer_info}

    def create_order_completed(self, order_info, db_connection):

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

        # 유저의 id를 넘겨주고, orders 테이블에 insert하는 메소드를 실행 후, 해당 order_no의 id(pk)를 가져옵니다.
        order_info['order_no'] = self.order_dao.insert_orders(order_info, db_connection)

        # orders_details를 insert하는 메소드를 실행 후, 생성된 테이블의 id(pk)를 order_info에 넣어줍니다.
        order_info['order_detail_no'] = self.order_dao.insert_orders_details(order_info, db_connection)

        # 서브쿼리를 줄이기 위해 메소드를 실행하여 product_option_no을 가져와 order_info에 넣어줍니다.
        product_option_no = self.order_dao.get_product_option_no(order_info, db_connection)

        # 위에서 반환된 product_option_no 타입은 딕셔너리이므로, order_info와 병합해 줍니다.
        order_info = {**order_info, **product_option_no}

        # order_product를 insert하는 메소드를 실행 후, 생성된 테이블의 id(pk)를 order_info에 넣어줍니다.
        order_info['order_product_no'] = self.order_dao.insert_order_product(order_info, db_connection)

        # 주문 정보에서 받아온 상품의 개수를 현재 재고에서 빼주는 메소드 입니다.
        self.order_dao.update_current_quantity(order_info, db_connection)

        # 원래 선분이력의 row id를 가져오는 메소드입니다.
        origin_quantity_info = self.order_dao.get_origin_quantity_no(order_info, db_connection)

        # 현재 옵션에 대한 재고의 선분이력을 관리해주는 quantities테이블을 생성하는 메소드 실행하여 id(pk)를 반홥해 줍니다.
        new_quantity_no = self.order_dao.insert_quantities(order_info, db_connection)

        # 선분이력을 관리하는 최신 재고에 대한 생성이력을 가져오는 메소드를 실행하여 start_time이라는 변수에 넣어줍니다.
        start_time = self.order_dao.get_quantity_start_time(new_quantity_no, db_connection)

        # quantities테이블에 선분이력 관리를 위해 새로 만들어준 선분에 해당하는 row의 정보 객체를 만들어줍니다.
        # 원래 재고의 선분이력 종료시간을 update해주기 위해 새로운 테이블의 생성시간을 가져옵니다.
        update_quantity_info = {
            "origin_quantity_no" : origin_quantity_info['quantity_no'], # 원래 있었던 선분의 no
            "start_time"         : start_time                           # 새로 생긴 선분의 start_time입니다.
        }
        # 선분이력을 관리하는 quantities 테이블의 종료시간에 새롭게 생성된 재고의 생성성시간을 넣어주는 메소드를 실행합니다.
        self.order_dao.update_quantities(update_quantity_info, db_connection)

        return 1

    def modify_user_shipping_details(self, order_info, db_connection):

        """

        상품 결제 시, 해당 유저의 배송지 정보가 없었다면, 받아온 배송지 정보를 Insert해주고,
        배송지 정보가 있었다면, 받아온 배송지 정보로 Update해줍니다.

        Args:
            order_info    : 유저의 id와 배송지 관련 정보가 들어있는 객체입니다.
            db_connection : 연결된 db 객체

        Returns:

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-09-06 (minho.lee0716@gmail.com) : 초기 생성
            2020-09-09 (minho.lee0716@gmail.com) : 수정
                user_shipping_details 테이블과 주문관련 테이블을 따로 작업하도록 메소드를 분리하였습니다.

        """

        # 해당 유저의 배송지 정보를 찾는 메소드를 실행하고, 먄악 배송지 정보가 존재 할 경우,
        if self.order_dao.select_user_shipping_details_info(order_info, db_connection):

            # 받아온 정보를 유저의 배송지 정보에 Update 해줍니다.
            self.order_dao.update_user_shipping_details_info(order_info, db_connection)

        # 해당 유저의 배송지 정보가 존재하지 않을 경우,
        else:

            # 받아온 정보를 유저의 배송지 정보에 Insert 해줍니다.
            self.order_dao.insert_user_shipping_details_info(order_info, db_connection)

        return 1

    def get_current_quantity(self, order_info, db_connection):

        """

        상품을 구매하기 전, 구매하려는 상품의 개수와 현재 상품의 재고를 비교해주는 메소드 입니다.

        Args:
            order_info    : 유저의 id와 배송지 관련 정보가 들어있는 객체입니다.
            db_connection : 연결된 db 객체

        Returns:

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-09-09 (minho.lee0716@gmail.com) : 초기 생성

        """

        # 해당 옵션의 상품 재고를 가져오기 위해 먼저 해당 상품의 id를 가져오는 메소드를 실행해 줍니다.
        product_option_no = self.order_dao.get_product_option_no(order_info, db_connection)

        # 해당 옵션의 상품 재고를 가져오기 위해 해당 상품 옵션의 id값을 인자로 넘겨주고 현재 재고를 받아옵니다.
        current_quantity = self.order_dao.get_current_quantity(product_option_no, db_connection)

        return current_quantity

    def get_product_quantity_range(self, product_info, db_connection):

        """

        

        Args:
            order_info    : 유저의 id와 배송지 관련 정보가 들어있는 객체입니다.
            db_connection : 연결된 db 객체

        Returns:

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-09-09 (minho.lee0716@gmail.com) : 초기 생성

        """

        # 해당 옵션의 상품 재고를 가져오기 위해 먼저 해당 상품의 id를 가져오는 메소드를 실행해 줍니다.
        product_option_no = self.order_dao.get_product_option_no(order_info, db_connection)

        # 해당 옵션의 상품 재고를 가져오기 위해 해당 상품 옵션의 id값을 인자로 넘겨주고 현재 재고를 받아옵니다.
        current_quantity = self.order_dao.get_current_quantity(product_option_no, db_connection)

        return current_quantity
