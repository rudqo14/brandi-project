from flask import jsonify

class UserDao:

    def signup_user(self, user_info, db_connection):

        """

        새로운 유저를 생성합니다.

        Args:
            user_info:
                name            : 회원명,
                email           : 이메일,
                social_id       : 소셜로그인 시 종류,
                user_social_id  : 소셜로그인 id
            db_connection : 연결된 db 객체

        Returns:
            생성된 유저 객체

            400 : KeyError

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-20 (tnwjd060124@gmail.com) : 초기 생성

        """

        with db_connection.cursor() as cursor:

            insert_user_query = """
            INSERT INTO users (
                name,
                email,
                social_id,
                user_social_id
            ) VALUES (
                %(name)s,
                %(email)s,
                %(social_id)s,
                %(user_social_id)s
            )
            """

            cursor.execute(insert_user_query, user_info)

            user = cursor.lastrowid
            return user

    def check_user(self, user_info, db_connection):

        """

        유저가 있는지 확인합니다.

        Args:
            user_info :
                user_no : pk
                email   : 이메일
            db_connection : 연결된 db 객체

        Returns:
            유저 객체

            400 : KeyError

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com): 초기 생성

        """

        with db_connection.cursor() as cursor:

            select_user_query = """
            SELECT
                user_no
            FROM
                users
            """
            for keys,values in user_info.items():
                if keys == 'email':
                    select_user_query += """
                    WHERE
                        email = %(email)s
                    """

                elif keys == 'user_no':
                    select_user_query += """
                    WHERE
                        user_no = %(user_no)s
                    """

            cursor.execute(select_user_query, user_info)

            user = cursor.fetchone()

            return user

    def check_social_user(self, user_info, db_connection):

        """

        소셜로그인 시 이미 생성된 소셜로그인id 가 있는지 확인합니다.

        Args:
            user_info :
                social_id       : 소셜로그인 시 종류,
                user_social_id  : 소셜로그인 id
            db_connection : 연결된 db 객체

        Returns:
            생성된 유저 객체

            400 : KeyError

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-20 (tnwjd060124@gmail.com) : 초기 생성

        """

        with db_connection.cursor() as cursor:

            select_user_query = """
            SELECT
                user_no
            FROM
                users
            WHERE
                social_id = %(social_id)s
                AND user_social_id = %(user_social_id)s
            """

            cursor.execute(select_user_query, user_info)

            user = cursor.fetchone()

            return user

    def get_user_password(self, user_info, db_connection):

        """

        유저의 비밀번호를 리턴합니다.

        Args:
            user_info:
                user_no : 유저의 pk
            db_connection : 연결된 db 객체

        Returns:
            유저의 password

            400 : KeyError

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com) : 초기 생성

        """

        with db_connection.cursor() as cursor:

            select_password_query = """
            SELECT
                password
            FROM
                users
            WHERE
                user_no = %(user_no)s
            """

            cursor.execute(select_password_query, user_info)

            password = cursor.fetchone()

            return password

    def update_user_last_access(self, user_info, db_connection):

        """

        유저의 최종 접속일을 업데이트 합니다.

        Args:
            user_info :
                user_no         : 유저의 pk
            db_connection : 연결된 db 객체

        Returns:

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com) : 초기 생성

        """

        with db_connection.cursor() as cursor:

            update_user_query = """
            UPDATE
                users
            SET
                last_access = CURRENT_TIMESTAMP
            WHERE
                user_no = %(user_no)s
            """

            cursor.execute(update_user_query, user_info)

            return cursor.lastrowid

    def get_user_list(self, filter_info, db_connection):

        """

        유저 리스트를 표출합니다.

        Args:
            filter_info : 필터 정보
            db_connection : 연결된 db 객체

        Returns:
            유저 리스트

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com) : 초기 생성
            2020-08-24 (tnwjd060124@gmail.com) : pagination 기능 추가
            2020-09-02 (tnwjd060124@gmail.com) : 필터 기능 추가

        """

        with db_connection.cursor() as cursor:

            select_user_query = """
            SELECT
                users.user_no,
                users.name,
                users.email,
                users.last_access,
                users.created_at,
                user_shipping_details.phone_number,
                social_networks.name AS social_name
            FROM
                users
            """

            select_user_query += """
            LEFT JOIN
                user_shipping_details
            ON users.user_no = user_shipping_details.user_id
            """

            # 계정 정보 filter 기능
            if filter_info['social_network']:
                select_user_query += """
                LEFT JOIN
                    social_networks
                ON users.social_id = social_networks.social_network_no
                AND social_networks.name = %(social_network)s
                """
            else:
                select_user_query += """
                LEFT JOIN
                    social_networks
                ON users.social_id = social_networks.social_network_no
                """

            # 삭제 되지 않은 데이터만 조회
            select_user_query += """
            WHERE
                users.is_deleted = 0
            """

            # 회원 번호 filter 기능
            if filter_info['user_no']:
                select_user_query += """
                AND users.user_no = %(user_no)s
                """

            # 회원명 filter 기능
            if filter_info['user_name']:
                select_user_query += """
                AND users.name = %(user_name)s
                """

            # 이메일 filter 기능
            if filter_info['email']:
                select_user_query += """
                AND users.email = %(email)s
                """

            # 최종 접속일 filter 기능
            if filter_info['lastaccess_from']:
                select_user_query += """
                AND users.last_access >= %(lastaccess_from)s
                """

            if filter_info['lastaccess_to']:
                select_user_query += """
                AND users.last_access <= %(lastaccess_to)s
                """

            # 등록일 filter 기능
            if filter_info['created_from']:
                select_user_query += """
                AND users.created_at >= %(created_from)s
                """

            if filter_info['created_to']:
                select_user_query += """
                AND users.created_at <= %(created_to)s
                """

            # 핸드폰 번호 filter 기능
            if filter_info['phone_number']:
                select_user_query += """
                AND user_shipping_details.phone_number = %(phone_number)s
                """
            if filter_info['sort'] :
                select_user_query += """
                ORDER BY
                    users.user_no DESC
                """
            else:
                select_user_query += """
                ORDER BY
                    users.user_no ASC
                """

            select_user_query += """
            LIMIT
                %(limit)s
            OFFSET
                %(offset)s
            """

            cursor.execute(select_user_query, filter_info)

            users = cursor.fetchall()

            return users

    def get_total_user(self, filter_info, db_connection):

        """

        총 유저의 수를 보여줍니다.

        Args:
            filter_info: filter 정보
            db_connection : 연결된 db 객체

        Returns:
            총 유저의 수

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-25 (tnwjd060124@gmail.com) : 초기 생성
            2020-09-02 (tnwjd060124@gmail.com) : 필터 기능 추가

        """

        with db_connection.cursor() as cursor:

            select_user_query = """
            SELECT
                COUNT(*) AS total_number
            FROM
                users
            """

            # 핸드폰 번호 filter 기능
            if filter_info['phone_number']:
                select_user_query += """
                LEFT JOIN
                    user_shipping_details
                ON users.user_no = user_shipping_details.user_id
                AND user_shipping_details.phone_number = %(phone_number)s
                """
            else:
                select_user_query += """
                LEFT JOIN
                    user_shipping_details
                ON users.user_no = user_shipping_details.user_id
                """

            # 계정 정보 filter 기능
            if filter_info['social_network']:
                select_user_query += """
                LEFT JOIN
                    social_networks
                ON users.social_id = social_networks.social_network_no
                AND social_networks.name = %(social_network)s
                """
            else:
                select_user_query += """
                LEFT JOIN
                    social_networks
                ON users.social_id = social_networks.social_network_no
                """

            # 삭제 되지 않은 데이터만 조회
            select_user_query += """
            WHERE
                users.is_deleted = 0
            """

            # 회원 번호 filter 기능
            if filter_info['user_no']:
                select_user_query += """
                AND users.user_no = %(user_no)s
                """

            # 회원명 filter 기능
            if filter_info['user_name']:
                select_user_query += """
                AND users.name = %(user_name)s
                """

            # 이메일 filter 기능
            if filter_info['email']:
                select_user_query += """
                AND users.email = %(email)s
                """

            # 최종 접속일 filter 기능
            if filter_info['lastaccess_from']:
                select_user_query += """
                AND users.last_access >= %(lastaccess_from)s
                """

            if filter_info['lastaccess_to']:
                select_user_query += """
                AND users.last_access <= %(lastaccess_to)s
                """

            # 등록일 filter 기능
            if filter_info['created_from']:
                select_user_query += """
                AND users.created_at >= %(created_from)s
                """

            if filter_info['created_to']:
                select_user_query += """
                AND users.created_at <= %(created_to)s
                """

            cursor.execute(select_user_query, filter_info)

            total_number = cursor.fetchone()

            return total_number

    def get_user_orders(self, user_info, db_connection):

        """

        유저의 주문 정보를 리턴합니다.

        Args:
            user_info:
                user_no : 유저의 pk
            db_connection : 연결된 db 객체

        Returns:
            유저의 주문 정보

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-28 (tnwjd060124@gmail.com) : 초기 생성
            2020-08-30 (tnwjd060124@gmail.com) : 수정
                제품 가격은 주문 생성시의 이력,
                제품명은 현재 이력으로 조회하도록 변경

        """

        with db_connection.cursor() as cursor:

            select_user_orders = """
            SELECT
                P2.order_detail_no,
                P2.start_time,
                P7.image_small,
                P12.product_no,
                P8.name AS product_name,
                P9.name AS color,
                P10.name AS size,
                P3.quantity,
                P8.price,
                P11.name AS order_status,
                CASE
                    WHEN P8.discount_rate IS NULL THEN 0
                    ELSE CASE
                        WHEN P8.discount_start_date IS NULL THEN P8.discount_rate
                        WHEN P2.start_time BETWEEN P8.discount_start_date AND P8.discount_end_date THEN P8.discount_rate
                        ELSE 0
                        END
                    END
                AS discount_rate

            FROM orders AS P1

            INNER JOIN orders_details AS P2
            ON P1.order_no = P2.order_id

            INNER JOIN order_product AS P3
            ON P2.order_detail_no = P3.order_detail_id

            INNER JOIN product_options AS P4
            ON P3.product_option_id = P4.product_option_no

            INNER JOIN option_details AS P5
            ON P4.product_option_no = P5.product_option_id
            AND P2.start_time >= P5.start_time
            AND P5.close_time >= P2.start_time

            INNER JOIN product_images AS P6
            ON P4.product_id = P6.product_id
            AND P6.is_main = 1
            AND P2.start_time >= P6.start_time
            AND P6.close_time >= P2.start_time

            INNER JOIN images AS P7
            ON P7.image_no = P6.image_id

            INNER JOIN product_details AS P8
            ON P4.product_id = P8.product_id
            AND P2.start_time >= P8.start_time
            AND P8.close_time >= P2.start_time

            INNER JOIN colors AS P9
            ON P9.color_no = P5.color_id

            INNER JOIN sizes AS P10
            ON P10.size_no = P5.size_id

            INNER JOIN order_status AS P11
            ON P11.order_status_no = P2.order_status_id

            INNER JOIN products AS P12
            ON P12.product_no = P4.product_id

            WHERE P1.user_id = %(user_no)s

            ORDER BY P1.order_no
            """

            cursor.execute(select_user_orders, user_info)

            orders = cursor.fetchall()

            return orders

    def get_user_order_detail(self, user_info, db_connection):

        """

        유저의 주문 상세 정보를 리턴합니다.

        Args:
            user_info:
                user_no : 유저의 pk
                order_detail_no : 주문 상세정보pk
            db_connection: 연결된 db 객체

        Returns:
            유저의 주문 상세정보

        Author:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-30 (tnwjd060124@gmail.com) : 초기 생성

        """

        with db_connection.cursor() as cursor:

            select_order_detail = """
            SELECT
                P1.order_detail_no,
                P1.start_time,
                P3.name AS orderer,
                P7.name AS product_name,
                P7.price,
                P9.image_small,
                P11.name AS color,
                P12.name AS size,
                P5.quantity,
                P13.name AS order_status,
                P4.receiver,
                P4.phone_number,
                P4.address,
                P4.additional_address,
                P4.delivery_request,
                CASE
                    WHEN P7.discount_rate IS NULL THEN 0
                    ELSE CASE
                        WHEN P7.discount_start_date IS NULL THEN P7.discount_rate
                        WHEN P1.start_time BETWEEN P7.discount_start_date AND P7.discount_end_date THEN P7.discount_rate
                        ELSE 0
                        END
                    END
                AS discount_rate

            FROM
                orders_details AS P1

            INNER JOIN orders AS P2
            ON P2.order_no = P1.order_id
            AND P2.user_id = %(user_no)s

            INNER JOIN users AS P3
            ON P2.user_id = P3.user_no

            INNER JOIN user_shipping_details AS P4
            ON P1.user_shipping_id = P4.user_shipping_detail_no

            INNER JOIN order_product AS P5
            ON P1.order_detail_no = P5.order_detail_id

            INNER JOIN product_options AS P6
            ON P6.product_option_no = P5.product_option_id

            INNER JOIN product_details AS P7
            ON P6.product_id = P7.product_id
            AND P1.start_time >= P7.start_time
            AND P7.close_time >= P1.start_time

            INNER JOIN product_images AS P8
            ON P6.product_id = P8.product_id

            INNER JOIN images AS P9
            ON P9.image_no = P8.image_id
            AND P1.start_time >= P9.start_time
            AND P9.close_time >= P1.start_time

            INNER JOIN option_details AS P10
            ON P6.product_option_no = P10.product_option_id
            AND P1.start_time >= P10.start_time
            AND P10.close_time >= P1.start_time

            INNER JOIN colors AS P11
            ON P10.color_id = P11.color_no

            INNER JOIN sizes AS P12
            ON P10.size_id = P12.size_no

            INNER JOIN order_status AS P13
            ON P1.order_status_id = P13.order_status_no

            WHERE
                P1.order_detail_no = %(order_detail_no)s
            """

            cursor.execute(select_order_detail, user_info)

            order_detail = cursor.fetchone()

            return order_detail

