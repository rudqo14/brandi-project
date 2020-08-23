from flask import jsonify

class UserDao:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def signup_user(self, user_info):
        """

        새로운 유저를 생성합니다.

        Args:
            user_info:
                name            : 회원명,
                email           : 이메일,
                social_id       : 소셜로그인 시 종류,
                user_social_id  : 소셜로그인 id

        Returns:
            생성된 유저 객체

            400 : KeyError

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-20 (tnwjd060124@gmail.com): 초기 생성

        """
        try:
            cursor = self.db_connection.cursor()
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
            self.db_connection.commit()

            user = cursor.lastrowid
            return user

        except KeyError:
            return jsonify({"message" : "KEY_ERROR"}), 400

    def check_user(self, user_info):
        """

        유저가 있는지 확인합니다.

        Args:
            user_info:
                email: 이메일

        Returns:
            유저 객체

            400 : KeyError

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com): 초기 생성

        """

        try:
            cursor = self.db_connection.cursor()

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

        except KeyError:
            return jsonify({"message" : "KEY_ERROR"}), 400

    def check_social_user(self, user_info):
        """

        소셜로그인 시 이미 생성된 소셜로그인id 가 있는지 확인합니다.

        Args:
            user_info:
                social_id : 소셜로그인 시 종류,
                user_social_id : 소셜로그인 id

        Returns:
            생성된 유저 객체

            400 : KeyError

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-20 (tnwjd060124@gmail.com) : 초기 생성

        """

        try:
            cursor = self.db_connection.cursor()

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

        except KeyError:
            return jsonify({"message" : 'KEY_ERROR'}), 400

    def get_user_password(self, user_info):
        """

        유저의 비밀번호를 리턴합니다.

        Args:
            user_info:
                user_no : 유저의 pk

        Returns:
            유저의 password

            400 : KeyError

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com) : 초기 생성

        """

        try:
            cursor = self.db_connection.cursor()

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

        except KeyError:
            return jsonify({"message" : "KEY_ERROR"}), 400

