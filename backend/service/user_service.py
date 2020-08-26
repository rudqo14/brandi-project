import time
import jwt

from config import SECRET

class UserService:

    def __init__(self, user_dao):
        self.user_dao = user_dao

    def sign_in(self, user_info, db_connection):
        """

        로그인 로직 구현

        Args:
            user_info :
                name        : 회원명,
                email       : 이메일,
                password    : 비밀번호
            db_connection : 연결된 db 객체

        Returns:
            user 객체

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-20 (tnwjd060124@gmail.com) : 초기 생성
            2020-08-21 (tnwjd060124@gmail.com) : 수정
                로그인 시 최종 접속일 업데이트 로직 추가
            2020-08-22 (tnwjd060124@gmail.com) : 수정
                dao 메소드 실행 시 db_connection을 parameter로 전달

        """
        # request로 들어온 정보와 일치하는 유저가 있는지 확인
        user = self.user_dao.check_user(user_info, db_connection)

        # 일치하는 유저가 없으면 None 리턴
        if not user:
            return None

        # 일치하는 유저가 있으면 해당 유저의 password 가져옴
        password = self.user_dao.get_user_password(user, db_connection)

        # request로 들어온 password와 db에 있는 password가 일치한지 확인
        if int(password['password']) != user_info['password']:
            return None

        # 비밀번호 일치 시 최종 접속 시간 업데이트
        self.user_dao.update_user_last_access(user, db_connection)


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

        # token 생성
        access_token = jwt.encode({'user_no' : user_no}, SECRET['secret_key'], SECRET['algorithm']).decode('utf-8')
        return access_token

    def google_social_login(self, user_info, db_connection):

        """

        구글 소셜 로그인 구현

        Args:
            user_info :
                user_email      : 이메일,
                user_name       : 유저명,
                user_social_id  : 유저의 social id
            db_connection : 연결된 db 객체

        Returns:
            user 객체

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com) : 초기 생성
            2020-08-21 (tnwjd060124@gmail.com) : 수정
                로그인 시 최종 접속일 업데이트 로직 추가
            2020-08-22 (tnwjd060124@gmail.com) : 수정
                dao 메소드 실행 시 db_connection을 parameter로 전달

        """
        # social_network 테이블의 구글pk 설정
        user_info['social_id'] = 1

        # db에 해당 소셜_id의 유저가 있는지 확인
        user = self.user_dao.check_social_user(user_info, db_connection)

        # 유저가 없으면 db에 유저 정보 저장
        if not user:
            user = self.user_dao.signup_user(user_info, db_connection)

        # 유저의 최종 접속시간 update
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.user_dao.update_user_last_access({
            'user_no'       : user['user_no'],
            'current_time'  : current_time
        }, db_connection)

        return user

    def get_user_list(self, page, limit, db_connection):

        """

        회원 관리에서 회원리스트를 보여줍니다.
        Args:
            page : 현재 페이지
            limit : page에 보여질 유저 수
            db_connection : 연결된 db 객체

        Returns:
            유저 목록

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-21 (tnwjd060124@gmail.com) : 초기 생성
            2020-08-22 (tnwjd060124@gmail.com) : 수정
                dao 메소드 실행 시 db_connection을 parameter로 전달
            2020-08-24 (tnwjd060124@gmail.com) : pagination 기능 추가

        """

        # offset 설정
        offset = (page*limit) - limit

        # 유저 리스트 가져오는 메소드 실행
        users = self.user_dao.get_user_list({
            "offset"    : offset,
            "limit"     : limit
        }, db_connection)

        return users

    def get_total_user_number(self, db_connection):

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

        # 총 유저의 수를 가져오는 메소드 실행
        total_number = self.user_dao.get_total_user(db_connection)

        return total_number
