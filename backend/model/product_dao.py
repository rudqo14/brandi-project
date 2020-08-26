from flask import jsonify

class ProductDao:

    def insert_product(self, db_connection):

        """

        product table insert function

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            200: SUCCESS, (상품등록 완료)

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-25 (sincerity410@gmail.com) : 초기생성
            2020-08-26 (sincerity410@gmail.com) : controller, service, model role 재정의에 따른 함수수정,
                                                  예외처리 추가

        """

        try:
            with db_connection.cursor() as cursor:

                # insert new product
                insert_product_query = """
                INSERT INTO products (
                    created_at,
                    is_deleted
                ) VALUES (
                    DEFAULT,
                    DEFAULT
                    )
                """

                # insert query execute
                affected_row = cursor.execute(insert_product_query)

                # check query execution
                if affected_row <= 0:
                    raise Exception('QUERY_FAILED')

                return cursor.lastrowid

        except Exception as e:
            raise e

    def insert_product_detail(self, product_info, db_connection):

        """

        상품등록 Model Function

        Args:
            product_info  : business layer로 부터 받은 Parameter
            db_connection : DATABASE Connection Instance

        Returns:
            200: SUCCESS, (상품등록 완료)

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-25 (sincerity410@gmail.com) : 초기생성
            2020-08-26 (sincerity410@gmail.com) : model role 재정의에 따라 함수분리 생성

        """

        try:
            with db_connection.cursor() as cursor:

                # insert product detail
                insert_product_detail_query = """
                INSERT INTO product_details (
                    product_id,
                    is_activated,
                    is_displayed,
                    main_category_id,
                    sub_category_id,
                    name,
                    simple_description,
                    detail_information,
                    price,
                    discount_rate,
                    discount_start_date,
                    discount_end_date,
                    min_sales_quantity,
                    max_sales_quantity
                ) VALUES (
                    %(product_id)s,
                    %(sellYn)s,
                    %(exhibitionYn)s,
                    %(mainCategoryId)s,
                    %(subCategoryId)s,
                    %(productName)s,
                    %(simpleDescription)s,
                    %(detailInformation)s,
                    %(price)s,
                    %(discountRate)s,
                    %(discountStartDate)s,
                    %(discountEndDate)s,
                    %(minSalesQuantity)s,
                    %(maxSalesQuantity)s
                )
                """

                # insert query execution
                affected_row = cursor.execute(insert_product_detail_query, product_info)

                # check query execution
                if affected_row <= 0:
                    raise Exception('QUERY_FAILED')

                return cursor.lastrowid

        except KeyError as e:
            raise e

        except Exception as e:
            raise e

    def insert_image(self, image_url, db_connection):

        """

        상품 이미지 URL 등록 -  Persistence Layer(model) function

        Args:
            image_url     : 사진 사이즈 별 URL(Dictionary)
                {
                    'product_image_L' : Large 사이즈 url,
                    'product_image_M' : Medium 사이즈 url,
                    'product_image_S' : Small 사이즈 url
                }
            db_connection : DATABASE Connection Instance

        Returns:
            등록한 image의 row id

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-28 (sincerity410@gmail.com) : 초기생성

        """

        try:
            with db_connection.cursor() as cursor:

                insert_images_query = """
                INSERT INTO images (
                    image_large,
                    image_medium,
                    image_small
                ) VALUES (
                    %(product_image_L)s,
                    %(product_image_M)s,
                    %(product_image_S)s
                )
                """

                affected_row = cursor.execute(insert_images_query, image_url)

                if affected_row <= 0 :
                    raise Exception('QUERY_FAILED')

                # 등록한 images 테이블의 row id Return
                return cursor.lastrowid

        except KeyError as e:
            raise e

        except Exception as e:
            raise e

    def insert_product_image(self, product_id, image_id, product_image_no, db_connection):

        """

        product_images(상품 이미지 id & 상품 id) 등록 -  Persistence Layer(model) function

        Args:
            product_id       : business layer로 부터 받은 Parameter
            image_id         : URL insert한 images 테이블의 row id
            product_image_no : image 순서 구분을 위한 image Number 정보(ex: product_image_1)
            db_connection    : DATABASE Connection Instance

        Returns:
            None

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-28 (sincerity410@gmail.com) : 초기생성

        """

        try:
            with db_connection.cursor() as cursor:

                # Thumbnail(대표) 사진의 구분
                is_main = 1 if product_image_no == 'product_image_1' else 0

                # Query Arguments를 정의할 변수
                product_image_info = {}

                # Function Arguments를 Query Arguments에 입력
                product_image_info['product_id'] = product_id
                product_image_info['image_id']   = image_id
                product_image_info['is_main']    = is_main

                insert_product_images_query = """
                INSERT INTO product_images (
                    product_id,
                    image_id,
                    is_main
                ) VALUES (
                    %(product_id)s,
                    %(image_id)s,
                    %(is_main)s
                )
                """

                affected_row = cursor.execute(insert_product_images_query, product_image_info)

                if affected_row <= 0 :
                    raise Exception('QUERY_FAILED')

                return None

        except KeyError as e:
            raise e

        except Exception as e:
            raise e

    def select_product_list(self, db_connection):

        """

        서비스 페이지의 상품 전체 리스트를 리턴합니다.

        Args:
            db_connection : 연결된 db 객체

        Returns:
            서비스 페이지의 상품 전체 리스트

        Authors:
            minho.lee0716@gmail.com (이민호)
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-25 (minho.lee0716@gmail.com) : 초기 생성
            2020-08-25 (minho.lee0716@gmail.com) : 수정
                컨벤션 수정
            2020-08-28 (tnwjd060124@gmail.com) : 현재 이력만 조회하는 조건 추가

        """

        with db_connection.cursor() as cursor:

            select_products_query = """
            SELECT
                P.product_no,
                I.image AS thumbnail_image,
                PD.name AS product_name,
                PD.price,
                PD.discount_rate

            FROM products as P

            LEFT JOIN product_images as PI
            ON P.product_no = PI.product_id
            AND CURRENT_TIMESTAMP >= PI.start_time
            AND PI.close_time >= CURRENT_TIMESTAMP
            AND PI.is_main = 1

            LEFT JOIN images as I
            ON PI.image_id = I.image_no
            AND I.is_deleted = 0

            LEFT JOIN product_details as PD
            ON P.product_no = PD.product_id
            AND PD.is_activated = 1
            AND PD.is_displayed = 1
            AND CURRENT_TIMESTAMP >= PD.start_time
            AND PD.close_time >= CURRENT_TIMESTAMP

            WHERE
                P.is_deleted = False

            ORDER BY
                P.product_no
            """

            cursor.execute(select_products_query)
            products = cursor.fetchall()

            return products

    def select_product_details(self, product_id, db_connection):

        """

        서비스 페이지의 상품 상세정보를 리턴합니다.

        Args:
            product_id    : 해당 상품의 id
            db_connection : 연결된 db 객체

        Returns:
            해당 상품에 대한 상세정보들

        Authors:
            minho.lee0716@gmail.com (이민호)

        History:
            2020-08-26 (minho.lee0716@gmail.com) : 초기 생성

        """

        with db_connection.cursor() as cursor:

            select_product_details_query = """
            """

            cursor.execute(select_product_details_query)
            product_details = cursor.fetchall()

            return product_details
