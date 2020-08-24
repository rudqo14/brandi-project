from flask      import Flask
from flask_cors import CORS

from model      import UserDao
from service    import UserService
from view       import create_user_endpoints, create_admin_user_endpoints

def create_app():
    """

    Returns :
        생성된 플라스크 앱 객체

    Authors :
        tnwjd060124@gmail.com (손수정)

    History :
        2020-08-19 (tnwjd060124@gmail.com) : 초기 생성

    """

    app = Flask(__name__)
    #CORS 설정
    CORS(app)
    #config 설정
    app.config.from_pyfile("config.py")
    # DAO 생성
    user_dao = UserDao()
    # Service 생성
    user_service = UserService(user_dao)
    # view blueprint 등록
    app.register_blueprint(create_user_endpoints(user_service))
    app.register_blueprint(create_admin_user_endpoints(user_service))

    return app
