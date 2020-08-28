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

        with db_connection.cursor() as cursro:

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

    def get_user_list(self, pagination, db_connection):

        """

        유저 리스트를 표출합니다.

        Args:
            pagination :
                limit : 가져올 row 개수
                offset : 앞의 생략할 row의 개수
            db_connection : 연결된 db 객체

        Returns:
            유저 리스트

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com) : 초기 생성
            2020-08-24 (tnwjd060124@gmail.com) : pagination 기능 추가

        """

        with db_connection.cursor() as cursor:

            select_user_query = """
            SELECT
                users.user_no,
                users.name,
                users.email,
                users.last_access,
                users.created_at,
                user_shipping_details.phone_number
            FROM
                users
            LEFT JOIN
                user_shipping_details
            ON
                users.user_no = user_shipping_details.user_id
            WHERE
                users.is_deleted = 0
            LIMIT
                %(limit)s
            OFFSET
                %(offset)s
            """

            cursor.execute(select_user_query, pagination)

            users = cursor.fetchall()

            return users

    def get_total_user(self, db_connection):

        """

        총 유저의 수를 보여줍니다.

        Args:
            db_connection : 연결된 db 객체

        Returns:
            총 유저의 수

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-25 (tnwjd060124@gmail.com) : 초기 생성

        """

        with db_connection.cursor() as cursor:

            select_number_query = """
            SELECT
                COUNT(*) AS total_number
            FROM
                users
            WHERE
                users.is_deleted = 0
            """

            cursor.execute(select_number_query)

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

        """

        with db_connection.cursor() as cursor:

            select_user_orders = """
            SELECT
                P2.order_detail_no,
                P2.start_time,
                P7.image_small,
                P8.name AS product_name,
                P9.name AS color,
                P10.name AS size,
                P3.quantity,
                P8.price,
                P11.name AS order_status

            FROM orders AS P1

            INNER JOIN orders_details AS P2
            ON P1.order_no = P2.order_id

            INNER JOIN order_product AS P3
            ON P2.order_detail_no = P3.order_id

            INNER JOIN product_options AS P4
            ON P3.product_option_id = P4.product_option_no

            INNER JOIN option_details AS P5
            ON P4.product_option_no = P5.product_option_id
            AND CURRENT_TIMESTAMP >= P5.start_time
            AND P5.close_time >= CURRENT_TIMESTAMP

            INNER JOIN product_images AS P6
            ON P4.product_id = P6.product_id
            AND P6.is_main = 1
            AND CURRENT_TIMESTAMP >= P6.start_time
            AND P6.close_time >= CURRENT_TIMESTAMP

            INNER JOIN images AS P7
            ON P7.image_no = P6.image_id

            INNER JOIN product_details AS P8
            ON P4.product_id = P8.product_id
            AND CURRENT_TIMESTAMP >= P8.start_time
            AND P8.close_time >= CURRENT_TIMESTAMP

            INNER JOIN colors AS P9
            ON P9.color_no = P5.color_id

            INNER JOIN sizes AS P10
            ON P10.size_no = P5.size_id

            INNER JOIN order_status AS P11
            ON P11.order_status_no = P2.order_status_id

            WHERE P1.user_id = %(user_no)s

            ORDER BY P1.order_no
            """

            cursor.execute(select_user_orders, user_info)

            orders = cursor.fetchall()

            return orders
