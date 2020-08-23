import jwt

from config import SECRET

class UserService:

    def __init__(self, user_dao):
        self.user_dao = user_dao

    def sign_in(self, user_info):
        """

        로그인 로직 구현

        Args:
            user_info:
                name : 회원명,
                email : 이메일,
                password : 비밀번호

        Returns:
            user 객체

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-20 (tnwjd060124@gmail.com) : 초기 생성

        """
        user = self.user_dao.check_user(user_info)

        if not user:
            return None

        password = self.user_dao.get_user_password({'user_no':user[0]})

        if int(password[0]) != user_info['password']:
            return None
        return user

    def generate_access_token(self, user_no):
        """

        jwt를 이용해 access token을 제공합니다.

        Args:
            user_no : 유저 pk

        Returns:
            access_token

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com) : 초기 생성

        """

        access_token = jwt.encode({'user_no' : user_no}, SECRET['secret_key'], SECRET['algorithm']).decode('utf-8')
        return access_token

    def google_social_login(self, user_info):

        """

        구글 소셜 로그인 구현

        Args:
            user_info:
                user_email      : 이메일,
                user_name       : 유저명,
                user_social_id  : 유저의 social id
        Returns:
            user 객체

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com) : 초기 생성

        """
        user_info['social_id'] = 1

        user = self.user_dao.check_social_user(user_info)

        if not user:
            user = self.user_dao.signup_user(user_info)

        return user
