import requests
from flask                  import request, Blueprint, jsonify
from flask_request_validator import (
    validate_params,
    Param,
    PATH,
    GET
)

from connection import get_connection
from utils      import (
    login_required,
    catch_exception,
    PageRule,
    LimitRule,
    DatetimeRule
)

def create_user_endpoints(user_service):

    user_app = Blueprint('user_app', __name__, url_prefix='/user')

    @user_app.route('/signin', methods=['POST'])
    def signin():

        """

        기본 로그인 api

        Args:
            email : 이메일
            password : 패스워드

        Returns:
            200, {"access_token" : access_token}
            401, {"message" : "UNAUTHORIZED"} : 로그인 실패(비밀번호or 이메일 불일치)
            500, {"message" : "NO_DATABASE_CONNECTION"} : db 연결 실패

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-20 (tnwjd060124@gmail.com) : 초기 생성
            2020-08-26 (tnwjd060124@gmail.com) : 수정
                controller에서 db commit하도록 변경

        """

        db_connection = None

        try:

            # db 연결
            db_connection = get_connection()

            # body 정보를 data에 저장
            data = request.json

            if db_connection:

                # 유저 로그인 메소드 실행
                sign_in_user = user_service.sign_in(data, db_connection)

                if sign_in_user:

                    #access_token 생성 메소드 실행 결과를 access_token 에 저장
                    access_token = user_service.generate_access_token(sign_in_user)

                    db_connection.commit()

                    return jsonify({'access_token' : access_token}), 200

                # login 실패
                return jsonify({'message' : 'UNAUTHORIZED'}), 401

            # db 연결되지 않은경우
            return jsonify({"message" : "NO_DATABASE_CONNECTION"}), 500

        # 정의하지 않은 에러 잡아줌
        except Exception as e:
            return jsonify({"message" : f'{e}'}), 500

        finally:
            if db_connection:
                db_connection.close()

    @user_app.route('/google-signin', methods=['POST'])
    def googlesignin():

        """

        구글 소셜 로그인 api

        Args:
            Authorization : 구글에서 받은 id_token

        Returns:
            200, {"access_token" : access_token}
            401, {"message" : "FAIL_SOCIAL_LOGIN"} : 로그인 실패
            500, {"message" : "NO_DATABASE_CONNECTION"} : db 연결 실패

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-20 (tnwjd060124@gmail.com) : 초기 생성
            2020-08-26 (tnwjd060124@gmail.com) : 수정
                controller에서 db commit하도록 변경

        """

        db_connection = None

        try:

            # db 연결
            db_connection = get_connection()

            if db_connection:

                # header에 담긴 token을 id_token에 저장
                id_token = request.headers['Authorization']

                # google oauth에 id_token을 담아 request 전송
                user_request = requests.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}')

                # request 결과를 user_info에 저장
                user_info = user_request.json()

                # 유저의 email, name, social_id 저장
                google_email = user_info.get('email')
                google_name = user_info.get('name')
                google_id = user_info.get('sub')

                # 저장된 결과로 소셜 로그인 메소드 실행, 결과를 sign_in_user에 저장
                sign_in_user = user_service.google_social_login(
                    {
                        "email"             : google_email,
                        "name"              : google_name,
                        "user_social_id"    : google_id
                    }, db_connection)

                if sign_in_user:

                    # 소셜 로그인 성공 시 access_token 생성 메소드 실행
                    access_token = user_service.generate_access_token(sign_in_user)

                    db_connection.commit()

                    return jsonify({"access_token" : access_token}), 200

                # 소셜 로그인 실패
                return jsonify({"message" : "FAIL_SOCIAL_LOGIN"}), 401

            # db 연결 되지 않았을 때
            return jsonify({"message" : "NO_DATABASE_CONNECTION"}), 500

        # 정의하지 않은 모든 에러를 잡아줌
        #except Exception as e:
            #return jsonify({"message" : f'{e}'}), 400

        finally:
            if db_connection:
                db_connection.close()

    @user_app.route('/mypage/orderlist', methods=['GET'])
    @login_required
    def get_user_orderlist(user_info):
        """

        유저 no에 따른 주문 정보를 리턴합니다.

        Args:
            headers:
                Authorization: access_token

            Returns:
                유저의 주문 정보

            Authors:
                tnwjd060124@gmail.com (손수정)

            History:
                2020-08-28 (tnwjd060124@gmail.com) : 초기 생성

        """

        db_connection = None

        try:

            # db 연결
            db_connection = get_connection()

            if db_connection:

                # 유저의 주문 정보를 가져오는 메소드 실행
                result = user_service.get_user_orders(user_info, db_connection)

                if result:

                    # 주문정보가 리턴
                    return jsonify({"data" : result}), 200

                # 주문정보가 없는 경우 빈 list 리턴
                return jsonify({"data" : []}), 200

            # db 연결이 되지 않은 경우
            return jsonify({"message" : "NO_DATABASE_CONNECTION"}), 500

        # 정의하지 않은 error를 잡아줌
        except Exception as e:
            return jsonify({"message" : f"{e}"}), 400

        finally:

            if db_connection:
                db_connection.close()

    @user_app.route('/mypage/orderdetail/<order_detail_no>', methods=['GET'], endpoint='user_order_detail')
    @catch_exception
    @validate_params(
        Param('order_detail_no', PATH, int)
    )
    @login_required
    def user_order_detail(user_info, *args):
        """

        유저의 주문 상세정보 표출 api

        Args:
            headers:
                Authorizaion: access_token

            Returns:
                200, 유저의 주문 상세정보
                401, 토큰에 해당하는 유저 정보 없을 시
                500, database 연결 실패

            Author:
                tnwjd060124@gmail.com (손수정)

            History:
                2020-08-30 (tnwjd060124@gmail.com) : 초기 생성

        """

        db_connection = None

        try:

            db_connection = get_connection()

            if db_connection:

                # path parameter로 받은 order_detail_no를 user_info에 넣어줌
                user_info['order_detail_no'] = args[0]

                result = user_service.get_order_detail(user_info, db_connection)

                if result:

                    return jsonify({"data" : result}), 200

                return jsonify({"message" : "NO_MATCH_DATA"}), 401

            # db 연결 실패
            return jsonify({"NO_DATABASE_CONNECTION"}), 500

        except Exception as e:
            return jsonify ({"message" : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    return user_app

def create_admin_user_endpoints(user_service):
    admin_user_app = Blueprint('admin_user_app', __name__, url_prefix='/admin/user')

    @admin_user_app.route('/userlist', methods=['GET'], endpoint='user_list')
    @catch_exception
    @validate_params(
        Param('page', GET, int, rules=[PageRule()]),
        Param('limit', GET, int, rules=[LimitRule()]),
        Param('lastAccessFrom', GET, int, required=False, rules=[DatetimeRule()]),
        Param('lastAccessTo', GET, int, required=False, rules=[DatetimeRule()]),
        Param('createdAtFrom', GET, int, required=False, rules=[DatetimeRule()]),
        Param('createdAtTo', GET, int, required=False, rules=[DatetimeRule()]),
        Param('userNo', GET, int, required=False),
        Param('userName', GET, str, required=False),
        Param('socialNetwork', GET, str, required=False),
        Param('phoneNumber', GET, int, required=False),
        Param('email', GET, str, required=False)
    )
    def user_list(*args):

        """

        유저 리스트 표출 api

        Args:
            page : 가져올 페이지
            limit : 가져올 갯수
            lastAccessFrom : 최종접속시간(from) filter
            lastAccessTo : 최종접속시간(to) filter
            createdAtFrom : 등록일 (from) filter
            createdAtTo : 등록일 (to) filter
            userNo : 회원번호 filter
            userName : 회원명 filter
            socialNetwork : 계정 정보 filter
            phoneNumber : 핸드폰 번호 filter
            email : 이메일 filter

        Returns:
            200, {
                "total_user_number" : 총 유저 수,
                "data"              : [
                    {
                        "created_at"    : 등록일,
                        "email"         : 이메일,
                        "last_access"   : 최종접속일,
                        "name"          : 회원명,
                        "phone_number"  : 휴대폰,
                        "user_no"       : 회원번호
            }]}
            500, {"message" : "NO_DATABASE_CONNECTION"} : db 연결 실패

        Authors:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-20 (tnwjd060124@gmail.com) : 초기 생성

        """

        db_connection = None

        try:

            # db 연결
            db_connection = get_connection()

            if db_connection:

                # request로 들어온 page, limit, filter 정보 저장
                filter_info = {
                    'page'            : args[0],
                    'limit'           : args[1],
                    'lastaccess_from' : args[2],
                    'lastaccess_to'   : args[3],
                    'created_from'    : args[4],
                    'created_to'      : args[5],
                    'user_no'         : args[6],
                    'user_name'       : args[7],
                    'social_network'  : args[8],
                    'phone_number'    : args[9],
                    'email'           : args[10]
                }

                # 총 유저의 수를 가져와서 total_user에 저장
                total_user = user_service.get_total_user_number(filter_info, db_connection)

                # 총 유저가 존재할 경우에만 유저리스트 가져옴
                if total_user['total_number']:

                    # 유저 리스트 가져와서 result에 저장
                    result = user_service.get_user_list(filter_info, db_connection)

                    return jsonify({"total_user_number" : total_user['total_number'], "data" : result}), 200

                # 총 유저가 없을 경우 빈 배열 리턴
                return jsonify({"total_user_number" : 0, "data" : []}), 200

            # db 연결 되지 않았을 때
            return jsonify({"message" : "NO_DATABASE_CONNECTION"}), 500

        # 정의하지 않은 모든 에러를 잡아줌
        except Exception as e:
            return jsonify({"message" : f'{e}'}), 500

        finally:
            if db_connection:
                db_connection.close()

    return admin_user_app
