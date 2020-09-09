from utils import ResizeImage, login_required
from decimal import *
from datetime import *

from flask import (
    request,
    Blueprint,
    jsonify
)
from flask_request_validator    import (
    GET,
    PATH,
    FORM,
    Param,
    Pattern,
    validate_params
)

from connection import get_connection, get_s3_connection
from utils      import (
    DatetimeRule,
    PageRule,
    LimitRule,
    catch_exception
)

def create_admin_product_endpoints(product_service):

    # 'admin/product' end point prefix 설정
    admin_product_app = Blueprint('product_app', __name__, url_prefix='/admin/product')

    @admin_product_app.route('', methods=['POST'])
    #@catch_exception
    @validate_params(
        Param('mainCategoryId', FORM, int),
        Param('subCategoryId', FORM, int),
        Param('sellYn', FORM, bool),
        Param('exhibitionYn', FORM, bool),
        Param('productName', FORM, str),
        Param('simpleDescription', FORM, str, required=False),
        Param('detailInformation', FORM, str),
        Param('price', FORM, float),
        Param('discountRate', FORM, int, required=False),
        Param('discountStartDate', FORM, str, required=False),
        Param('discountEndDate', FORM, str, required=False),
        Param('minSalesQuantity', FORM, int),
        Param('maxSalesQuantity', FORM, int),
        Param('optionQuantity', FORM, str, required=False)
    )
    def product_register(*args):

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
            2020-09-02 (sincerity410@gmail.com) : product_code column 추가에 따른 구조 수정
            2020-09-08 (sincerity410@gmail.com) : request Validation Check 추가

        """

        # finally error 발생 방지
        db_connection = None

        try:

            db_connection = get_connection()

            if db_connection:

                product_info = {
                    'mainCategoryId'    : args[0],
                    'subCategoryId'     : args[1],
                    'sellYn'            : args[2],
                    'exhibitionYn'      : args[3],
                    'productName'       : args[4],
                    'simpleDescription' : args[5],
                    'detailInformation' : args[6],
                    'price'             : args[7],
                    'discountRate'      : args[8],
                    'discountStartDate' : args[9],
                    'discountEndDate'   : args[10],
                    'minSalesQuantity'  : args[11],
                    'maxSalesQuantity'  : args[12],
                    'optionQuantity'    : args[13]
                }

                product_info_process = {}

                for key, value in product_info.items():
                    if value != 'null':
                        product_info_process[key] = value
                    else:
                        product_info_process[key] = None

                # 사이즈 별(Large, Medium, Small) 상품이미지 저장 위한 S3 Connection Instance 생성
                s3_connection = get_s3_connection()
                images        = request.files

                # 상품정보를 DB에 저장하는 Function 실행
                product_id = product_service.create_product(product_info_process, db_connection)

                # 상품이미지를 사이즈 별로 S3에 저장 및 URL을 DB에 Insert 하는 Function 실행
                product_service.upload_product_image(
                    images,
                    product_id,
                    s3_connection,
                    db_connection
                )

                # Exception이 발생하지 않았다면, commit 처리
                db_connection.commit()

                return jsonify({'message' : 'SUCCESS'}), 200

        #except Exception as e:
        #    db_connection.rollback()
        #    return jsonify({"message" : f'{e}'}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('/option', methods=['GET'])
    def option_list():

        """

        [ 상품관리 > 상품등록] 옵션(색상, 사이즈) List Return 엔드포인트
        [GET] http://ip:5000/admin/product/option

        Returns:
            200 :
                "data" : [
                    "color":[
                        {
                            "color_no" : {color_no} ,
                            "name"     : "{color_nam}"
                        }
                    ]
                    "size":[
                        {
                            "size_no" : {size_no},
                            "name"    : "{size_name}"
                        }
                    ]
                ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성
            2020-09-02 (sincerity410@gmail.com) : 옵션(색상, 사이즈) 통합 형태로 제공

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()
            if db_connection:

                # get_option_list 함수 호출해 색상 List 받아오기
                options = product_service.get_option_list(db_connection)

                return jsonify({'data' : options}), 200

        except Exception as e:
            return jsonify({'message' : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('/category', methods=['GET'])
    def main_category_list():

        """

        [ 상품관리 > 상품등록] Main Category Return 엔드포인트
        [GET] http://ip:5000/admin/product/category

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

        except Exception as e:
            return jsonify({'message' : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('/category/<main_category_id>', methods=['GET'])
    @catch_exception
    @validate_params(
        Param('main_category_id', PATH, int)
    )
    def sub_category_list(*args):

        """

        [ 상품관리 > 상품등록] Sub Category Return 엔드포인트
        [GET] http://ip:5000/admin/product/category/<main_category_id>

        Args:
            Parameter:
                mainCategoryId : (int) 메인 카테고리 ID

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

                main_category_id = args[0]

                # sub_category_list 함수 호출해 Sub Category List 받아오기
                sub_category = product_service.get_sub_category_list(main_category_id, db_connection)

                return jsonify({'data' : sub_category}), 200

        except Exception as e:
            return jsonify({'message' : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('', methods=['GET'])
    #catch_exception
    @validate_params(
        Param('sellYn', GET, bool, required=False),
        Param('discountYn', GET, bool, required=False),
        Param('exhibitionYn', GET, bool, required=False),
        Param('startDate', GET, int, required=False, rules=[DatetimeRule()]),
        Param('endDate', GET, int, required=False, rules=[DatetimeRule()]),
        Param('productName', GET, str, required=False),
        Param('productNo', GET, int, required=False),
        Param('productCode', GET, str, required=False),
        Param('page', GET, int, rules=[PageRule()]),
        Param('limit', GET, int, rules=[LimitRule()])
    )

    def registered_product_list(*args):

        """

        [ 상품관리 > 상품등록] Sub Category Return 엔드포인트
        [GET] http://ip:5000/admin/product

        Args:
            Parameter: 미적용시 filter에서 제외
                sellYN       : 판매 여부(1|0)
                exhibitionYn : 진열 여부(1|0)
                discountYn   : 할인 여부(1|0)
                registDate   : 등록 일자(기준 시작일, 기준 종료일)
                {
                    startDate : "YYYYmmdd",
                    endDate   : "YYYYmmdd"
                }
                productName  : 상품 이름
                productNo    : 상품 번호
                productCode  : 상품 코드
                limit        : 페이지 당 상품 수
                page         : 페이지 리스트 시작 기준

        Returns:
            200 :
                "data": [
                    [
                        {
                            discountPrice        : 할인가
                            discountRate         : 할인율
                            discountYn           : 할인 여부
                            productCode          : 상품 코드
                            productExhibitYn     : 진열 여부
                            productName          : 상품 이름
                            productNo            : 상품 번호
                            productRegistDate    : 상품 등록 일시
                            productSellYn        : 판매 여부
                            productSmallImageUrl : SMALL SIZE IMAGE URL
                            sellPrice            : 상품 가격
                        }
                    ],
                        {
                            "total": 검색된 상품 개수
                        }
                ]
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-31 (sincerity410@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:

                filter_info = {
                    'sellYn'       : args[0],
                    'discountYn'   : args[1],
                    'exhibitionYn' : args[2],
                    'startDate'    : args[3],
                    'endDate'      : args[4],
                    'productName'  : args[5],
                    'productNo'    : args[6],
                    'productCode'  : args[7],
                    'page'         : args[8],
                    'limit'        : args[9]
                }

                # 상품 List, Totacl Count 받는 service 함수 호출 
                product_list = product_service.get_registered_product_list(filter_info, db_connection)

                return jsonify({'data' : product_list}), 200

        #except Exception as e:
        #    return jsonify({'message' : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('/detail-image', methods=['POST'])
    def product_detail_image_upload():

        """

        [상품관리 > 상품등록] - 엔드포인트 Function
        [POST] http://ip:5000/admin/product/detail-image

        Args:
            request.files
                product_detail_image_url : 상품 상세 image URL

        Returns:
            200 : 상품 상세 image URL
            400 : VALIDATION_ERROR, KEY_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-03 (sincerity410@gmail.com) : 초기 생성
            2020-09-04 (sincerity410@gmail.com) : CKEditor 양식에 맞춰 수정

        """

        try:
            # 상품의 상세 설명 이미지의 저장을 위한 S3 Connection Instance 생성
            s3_connection = get_s3_connection()
            image         = request.files

            # 상품의 상세 설명 이미지의 S3 저장을 위한 Function 실행
            image_url_info = product_service.upload_detail_image(
                image,
                s3_connection
            )

            return jsonify(image_url_info), 200

        except Exception as e:
            return jsonify({'message' : f"{e}"}), 400

    @admin_product_app.route('/<product_id>', methods=['GET'])
    #@catch_exception
    @validate_params(
        Param('product_id', PATH, int)
    )
    def product_detail(*args):

        """

        [ 상품관리 > 상품등록] 상품 수정을 위한 Detail 내역 Return 엔드포인트
        [GET] http://ip:5000/admin/product/<product_id>

        Args:
            Parameter:
                productId : (int) Product Id(상품 테이블 PK)

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
            2020-09-05 (sincerity410@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            if db_connection:

                product_id = args[0]

                # sub_category_list 함수 호출해 Sub Category List 받아오기
                product_info = product_service.get_product_detail(product_id, db_connection)

                return jsonify({'data' : product_info}), 200

        #except Exception as e:
        #    return jsonify({'message' : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    @admin_product_app.route('/<product_id>', methods=['PUT'])
    #@catch_exception
    @validate_params(
        Param('product_id', PATH, int),
        Param('mainCategoryId', FORM, int),
        Param('subCategoryId', FORM, int),
        Param('sellYn', FORM, int, required=False),
        Param('exhibitionYn', FORM, int, required=False),
        Param('productName', FORM, str, required=False),
        Param('simpleDescription', FORM, str, required=False),
        Param('detailInformation', FORM, str, required=False),
        Param('price', FORM, float),
        Param('discountRate', FORM, int),
        Param('discountStartDate', FORM, str, required=False),
        Param('discountEndDate', FORM, str, required=False),
        Param('minSalesQuantity', FORM, int),
        Param('maxSalesQuantity', FORM, int),
        Param('optionQuantity', FORM, str, required=False)
    )
    def product_modify(*args):

        """

        [상품관리 > 상품등록] - 엔드포인트 Function
        [PUT] http://ip:5000/admin/product

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
            2020-09-06 (sincerity410@gmail.com) : 초기생성

        """

        # finally error 발생 방지
        db_connection = None

        try:

            db_connection = get_connection()

            if db_connection:

                product_id   = args[0]
                product_info = {
                    'mainCategoryId'    : args[1],
                    'subCategoryId'     : args[2],
                    'sellYn'            : args[3],
                    'exhibitionYn'      : args[4],
                    'productName'       : args[5],
                    'simpleDescription' : args[6],
                    'detailInformation' : args[7],
                    'price'             : args[8],
                    'discountRate'      : args[9],
                    'discountStartDate' : args[10],
                    'discountEndDate'   : args[11],
                    'minSalesQuantity'  : args[12],
                    'maxSalesQuantity'  : args[13],
                    'optionQuantity'    : args[14]
                }

                # DB 저장 내역과 비교를 위한 price value Decimal 변경
                product_info['price'] = round(Decimal(product_info['price']),2)

                # DB 저장 내역과 비교를 위한 discountStartDate, discountEndDate datetime 형태로 변경
                if product_info['discountStartDate'] is not None:
                    product_info['discountStartDate'] = datetime.strptime(product_info['discountStartDate'], '%Y-%m-%d')
                if product_info['discountEndDate'] is not None:
                    product_info['discountEndDate'] = datetime.strptime(product_info['discountEndDate'], '%Y-%m-%d')

                # 사이즈 별(Large, Medium, Small) 상품이미지 저장 위한 S3 Connection Instance 생성
                s3_connection = get_s3_connection()
                images        = request.files

                # 상품정보를 DB에 저장하는 Function 실행
                product_service.update_product(product_id, product_info, db_connection)

                # 상품이미지를 사이즈 별로 S3에 저장 및 URL을 DB에 Insert 하는 Function 실행
                #product_service.upload_product_image(
                #    images,
                #    product_id,
                #    s3_connection,
                #    db_connection
                #)

                # Exception이 발생하지 않았다면, commit 처리
                db_connection.commit()

                return jsonify({'message' : 'SUCCESS'}), 200

        #except Exception as e:
        #    db_connection.rollback()
        #    return jsonify({"message" : f'{e}'}), 400

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
            200 : "data": [
                        {
                          "discount_rate": 30,
                          "price": 11250.0,
                          "product_name": "반팔티",
                          "product_no": 1,
                          "thumbnail_image": "(생략)~M.jpg"
                        },
                        {
                          "discount_rate": 20,
                          "price": 11110.0,
                          "product_name": "티셔츠",
                          "product_no": 2,
                          "thumbnail_image": "(생략)~M.jpg"
                        },
                        {
                          "discount_rate": 30,
                          "price": 13700.0,
                          "product_name": "티셔츠",
                          "product_no": 3,
                          "thumbnail_image": "(생략)~M.jpg"
                        }
                  ]
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

    @service_product_app.route('/<product_id>', methods=['GET'])
    @catch_exception
    @validate_params(
        Param('product_id', PATH, int)
    )
    def product_details(product_id):

        """

        [ 서비스 > 상품 상세정보 ] 엔드포인트
        [GET] http://ip:5000/product/1

        Args:
            Query Parameter:
                product_id : 상품의 id

        Returns:
            200 : 상품에 대한 상세정보
            400 : VALIDATION_ERROR
            401 : product_id에 해당하는 상품이 없는경우
            500 : NO_DATABASE_CONNECTION_ERROR

        [ 서비스 > 상품 상세정보 > 나머지 옵션 ] 엔드포인트
        [GET] http://ip:5000/product/1?color_id=1

        Args:
            Query Parameter:
                product_id : 상품의 id
                color_id   : 상품에 대한 색상의 id

        Returns:
            200 : 상품의 색상에 해당되는 색상과 재고
            400 : KEY_ERROR
            400 : THIS_COLOR_DOES_NOT_EXISTS
            400 : VALIDATION_ERROR
            500 : NO_DATABASE_CONNECTION_ERROR


        Author:
            minho.lee0716@gmail.com (이민호)
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-27 (minho.lee0716@gmail.com) : 초기생성
            2020-09-01 (minho.lee0716@gmail.com) : 수정
                상품의 상세정보와 이미지, 컬러까지만 리턴을 해주도록 수정
            2020-09-02 (minho.lee0716@gmail.com) : 수정
                product_etc_options 라는 함수를 없애고 이 엔드포인트에 query parameter로
                색상의 조건이 들어올 시, 나머지 사이즈와 재고를 리턴
            2020-09-09 (tnwjd060124@gmail.com) : 수정
                path parameter로 들어온 product_id에 해당하는 제품이 없을 때 401에러 리턴

        """

        # finally error 발생 방지
        db_connection = None

        try:
            db_connection = get_connection()

            # DB에 연결이 됐다면
            if db_connection:

                # service에서 상세정보, 이미지, 옵션을 묶은 정보들을 details에 저장
                details = product_service.get_product_details(product_id, db_connection)

                # 상품id에 해당하는 정보가 존재하는 경우에만 실행
                if details:

                    # Query Parameter의 요청이 존재할 경우
                    if request.args:

                        # color_id로 들어온 키의 값을 color_id라는 변수에 저장
                        color_id = request.args['color_id']

                        # 나머지 옵션을 가져오기 위해 딕셔너리를 생성
                        product_info = {
                            'product_id' : product_id,
                            'color_id'   : color_id
                        }

                        # service에서 나머지 옵션(사이즈, 재고)을 묶은 정보들을 etc_options에 저장
                        # 나머지 옵션들의 정보가 없다면 service에서 raise를 이용한 에러 처리
                        etc_options = product_service.get_etc_options(product_info, db_connection)

                        return jsonify({'data' : etc_options}), 200

                    return jsonify({'data' : details}), 200

                # 상품 id에 해당하는 data가 존재하지 않은 경
                return jsonify({'message' : 'NON_EXISTING_DATA'}), 401

            # DB에 연결이 되지 않았을 경우, DB에 연결되지 않았다는 에러메시지를 보내줍니다.
            return jsonify({'message' : 'NO_DATABASE_CONNECTION'}), 500

        # 요청은 들어오지만, Query Parameter의 키 값이 잘못 요청된 경우
        except KeyError:
            return jsonify({'message' : 'KEY_ERROR'}), 400

        except Exception as e:
            return jsonify({'message' : f"{e}"}), 400

        finally:
            if db_connection:
                db_connection.close()

    return service_product_app
