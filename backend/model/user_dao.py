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
        cursor = db_connection.cursor()
        create_user = """
        INSERT INTO users
        (
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

        cursor.execute(create_user, user_info)

        user = cursor.lastrowid
        return user

    def check_user(self, user_info, db_connection):
        """

        유저가 있는지 확인합니다.

        Args:
            user_info :
                email : 이메일
            db_connection : 연결된 db 객체

        Returns:
            유저 객체

            400 : KeyError

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com): 초기 생성

        """

        cursor = db_connection.cursor()

        select_user = """
        SELECT
            user_no
        FROM
            users
        WHERE
            email = %(email)s
        """

        cursor.execute(select_user, user_info)
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

        cursor = db_connection.cursor()

        select_user = """
        SELECT
            user_no
        FROM
            users
        WHERE
            social_id = %(social_id)s
            AND user_social_id = %(user_social_id)s
        """
        cursor.execute(select_user, user_info)
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

        cursor = db_connection.cursor()

        select_password = """
        SELECT
            password
        FROM
            users
        WHERE
            user_no = %(user_no)s
        """
        cursor.execute(select_password, user_info)
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

        cursor = db_connection.cursor()

        update_user = """
        UPDATE
            users
        SET
            last_access = CURRENT_TIMESTAMP
        WHERE
            user_no = %(user_no)s
        """
        cursor.execute(update_user, user_info)
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

        cursor = db_connection.cursor()

        select_users = """
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

        cursor.execute(select_users, pagination)
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

        cursor = db_connection.cursor()

        get_number = """
        SELECT
            COUNT(*) AS total_number
        FROM
            users
        WHERE
            users.is_deleted = 0
        """

        cursor.execute(get_number)
        total_number = cursor.fetchone()

        return total_number
