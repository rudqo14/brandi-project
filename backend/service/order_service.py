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

    def check_filter_list(self, filter_info, search_info):
        """

        filter의 유효성 체크

        Args:
            filter_info:
                page : 현재 페이지
                limit : 가져올 row 갯수
                from_date : 날짜 filter
            search_info:
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
            if not any(search_info.values()):
                return None

        # filter_info에 검색 정보들 저장
        for key,values in search_info.items():
            if values:
                filter_info[key] = values
            else:
                filter_info[key] = '%'

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
