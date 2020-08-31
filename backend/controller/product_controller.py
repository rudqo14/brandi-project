from utils      import ResizeImage

from flask import (
    request,
    Blueprint,
    jsonify
)

from connection import get_connection, get_s3_connection

def create_admin_product_endpoints(product_service):

    # 'admin/product' end point prefix 설정
    admin_product_app = Blueprint('product_app', __name__, url_prefix='/admin/product')

    # 상품등록 Function
    @admin_product_app.route('', methods=['POST'])
    def product_register():

        """

        [상품관리 > 상품등록] - 엔드포인트 Function
        [POST] http://ip:5000/admin/product

        Args:
            request.form:
                mainCategoryId      : Main Category ID
                subCategoryId       : Sub Category ID
                sellYn              : 상품 판매여부 (Boolean)
                exhibitionYn        : 상품 진열여부 (Boolean)
                productName         : 상품이름
                simpleDescription   : 상품 한 줄 설명
                detailInformation   : 상품 상세 설명
                price               : 상품가격
                discountRate        : 상품 할인율
                discountStartDate   : 할인 시작일
                discountEndDate     : 할인 종료일
                minSalesQuantity    : 최소판매 수량
                maxSalesQuantity    : 최대판매 수량
                optionQuantity      : 옵션별 수량 List
                    {
                        colorId  : 상품 색상 id
                        sizeId   : 상품 사이즈 id
                        quantity : 상품 재고수량
                    }

            request.files
                product_image_(No.) : 상품이미지 파일(Number: 1-5)

        Returns:
            200 : SUCCESS, 상품등록 완료 message
            400 : VALIDATION_ERROR, KEY_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-25 (sincerity410@gmail.com) : 초기생성
            2020-08-26 (sincerity410@gmail.com) : controller, service, model role 재정의에 따른 함수수정
            2020-08-28 (sincerity410@gmail.com) : product_images, images 저장 기능추가
            2020-08-30 (sincerity410@gmail.com) : product option 별 재고수량 저장 기능추가

        """

        # finally error 발생 방지
        db_connection = None

        try:

            db_connection = get_connection()

            # 사이즈 별(Large, Medium, Small) 상품이미지 저장 위한 S3 Connection Instance 생성
            s3_connection = get_s3_connection()
            images        = request.files

            # 상품이미지를 사이즈 별로 S3에 저장하는 Function 실행  
            product_image_upload_result  = product_service.upload_product_image(images, s3_connection)

            if db_connection:

                # form-data request를 product_info라는 Dictionary 변수에 담기
                product_info = request.form.to_dict(flat=False)

                # 1-5번의 사이즈 별 상품이미지를 product_info에 추가
                product_info['image_url'] = product_image_upload_result

                # 상품정보를 DB에 저장하는 Function 실행
                product_service.create_product(product_info, db_connection)
                db_connection.commit()

                return jsonify({'message' : 'SUCCESS'}), 200

        except Exception as e:
            db_connection.rollback()
            return jsonify({"message" : f'{e}'}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('/color', methods=['GET'])
    def color_list():

        """

        [ 상품관리 > 상품등록] 색상 List Return 엔드포인트
        [GET] http://ip:5000/admin/product/color

        Returns:
            200 :
                "data" : [
                    {
                        "color_no" : {color_no} ,
                        "name"     : "{color_nam}"
                    }
                ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:

                # get_size_list 함수 호출해 색상 List 받아오기
                colors = product_service.get_color_list(db_connection)

                return jsonify({'data' : colors}), 200

        except Exception as e:
            return jsonify({'message' : e}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('/size', methods=['GET'])
    def size_list():

        """

        [ 상품관리 > 상품등록] 사이즈 List Return 엔드포인트
        [GET] http://ip:5000/admin/product/size

        Returns:
            200 :
                "data": [
                    {
                        "size_no" : {size_no},
                        "name"    : "{size_name}"
                    }
                ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:

                # get_size_list 함수 호출해 사이즈 List 받아오기
                sizes = product_service.get_size_list(db_connection)

                return jsonify({'data' : sizes}), 200

        except Exception as e:
            return jsonify({'message' : e}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('/main-category', methods=['GET'])
    def main_category_list():

        """

        [ 상품관리 > 상품등록] Main Category Return 엔드포인트
        [GET] http://ip:5000/admin/product/main-category

        Returns:
            200 :
                "data": [
                    {
                      "main_category_no" : {main_category_id},
                      "name"             : "{main_category_name}"
                    }
                ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-30 (sincerity410@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:

                # get_main_category_list 함수 호출해 Main Category List 받아오기
                main_category = product_service.get_main_category_list(db_connection)

                return jsonify({'data' : main_category}), 200

        #except Exception as e:
        #    return jsonify({'message' : e}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('/sub-category', methods=['POST'])
    def sub_category_list():

        """

        [ 상품관리 > 상품등록] Sub Category Return 엔드포인트
        [POST] http://ip:5000/admin/product/sub-category

        Args:
            request.body:
                mainCategoryId : 메인 카테고리 ID

        Returns:
            200 :
                "data": [
                    {
                      "name"            : "{sub_category_name}",
                      "sub_category_no" : {sub_category_no}
                    }
                ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-30 (sincerity410@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:

                main_cetegory_id = request.json['mainCategoryId']

                # sub_category_list 함수 호출해 Sub Category List 받아오기
                sub_category = product_service.get_sub_category_list(main_cetegory_id, db_connection)

                return jsonify({'data' : sub_category}), 200

        #except Exception as e:
        #    return jsonify({'message' : e}), 400

        finally:
            if db_connection:
                db_connection.close()

    return admin_product_app

def service_product_endpoint(product_service):

    # '/product' end point prefix 설정
    service_product_app = Blueprint('service_product_app', __name__, url_prefix='/product')

    @service_product_app.route('', methods=['GET'])
    def product_list():

        """

        [ 서비스 > 상품 전체 리스트 ] 엔드포인트
        [GET] http://ip:5000/product

        Returns:
            200 : data, [ 서비스 > 상품 전체 리스트 ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-08-25 (minho.lee0716@gmail.com) : 초기생성
            2020-08-26 (minho.lee0716@gmail.com) : 수정
                엔드포인트를 찾아가지 못하는 문제 해결
            2020-08-27 (minho.lee0716@gmail.com) : 수정
                상품이 하나도 존재하지 않을 경우 빈 배열을 리턴

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            # DB에 연결이 잘 되었을 경우
            if db_connection:

                # 모든 상품을 products라는 변수에 가져와 담습니다.
                products = product_service.get_product_list(db_connection)

                # 상품이 1개라도 존재하지 않을 경우 json 리턴값이 null 인걸 확인하였고, 그럴 경우엔
                if not products:
                    # 빈 배열을 리턴해줍니다.
                    return jsonify({'data' : []}), 200

                # 상품이 1개 이상 존재할 경우, 모든 상품 리스트를 리턴해줍니다.
                return jsonify({'data' : products}), 200

            # DB에 연결이 되지 않았을 경우, DB에 연결되지 않았다는 에러메시지를 보내줍니다.
            return jsonify({'message' : 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message' : e}), 400

        finally:
            if db_connection:
                db_connection.close()

    @service_product_app.route('/<int:product_id>', methods=['GET'])
    def product_details(product_id):

        """

        [ 서비스 > 상품 상세정보 ] 엔드포인트
        [GET] http://ip:5000/product/product_id

        Returns:
            200 : data, [ 서비스 > 상품 상세정보 ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-08-27 (minho.lee0716@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:
                print(product_id)
                details = product_service.get_product_details(product_id, db_connection)
                return jsonify({'data' : details}), 200

        except Exception as e:
            return jsonify({'message' : e}), 400

        finally:
            if db_connection:
                db_connection.close()

    return service_product_app
