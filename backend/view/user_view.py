import requests

from flask import request, Blueprint, jsonify

def create_user_endpoints(user_service):
    user_app = Blueprint('user_app', __name__, url_prefix='/user')

    @user_app.route('/signin', methods=['POST'])
    def signin():
        data = request.json
        sign_in_user = user_service.sign_in(data)

        if sign_in_user:
            #access_token 생성
            access_token = user_service.generate_access_token(sign_in_user)

            return jsonify({'access_token' : access_token}), 200

        return jsonify({'message' : 'UNAUTHORIZED'}), 401

    @user_app.route('/google-signin', methods=['POST'])
    def googlesignin():
        id_token = request.headers['Authorization']
        user_request = requests.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}')

        user_info = user_request.json()
        google_email = user_info.get('email')
        google_name = user_info.get('name')
        google_id = user_info.get('sub')

        sign_in_user = user_service.google_social_login(
            {
                "email"             : google_email,
                "name"              : google_name,
                "user_social_id"    : google_id
            })

        if sign_in_user:
            access_token = user_service.generate_access_token(sign_in_user)
            return jsonify({"access_token" : access_token}), 200

    return user_app
