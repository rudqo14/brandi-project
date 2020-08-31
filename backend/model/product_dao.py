class ProductDao:

    def insert_product(self, db_connection):

        """

        상품 테이블(products)에 insert 하고 product_no(PK)를 Return 합니다.

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            product_no(products Table PK)

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

        상품 상세 테이블(product_details)에 insert 합니다.

        Args:
            product_info  : business layer로 부터 받은 Parameter
            db_connection : DATABASE Connection Instance

        Returns:
            None

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

                return None

        except KeyError as e:
            raise e

        except Exception as e:
            raise e

    def insert_image(self, image_url, db_connection):

        """

        상품 이미지 URL을 Image Size 별로 images 테이블에 insert 하고 image_no(PK)를 Return합니다.

        Args:
            image_url     : 사진 사이즈 별 URL(Dictionary)
                {
                    'product_image_L' : Large 사이즈 url,
                    'product_image_M' : Medium 사이즈 url,
                    'product_image_S' : Small 사이즈 url
                }
            db_connection : DATABASE Connection Instance

        Returns:
            image_no(images Table PK)

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

        products와 images 테이블의 중간 테이블(product_images)에 상품별 image row id를 insert 합니다.

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

                insert_product_images_query = """
                INSERT INTO product_images (
                    product_id,
                    image_id,
                    is_main
                ) VALUES (
                    %s,
                    %s,
                    %s
                )
                """

                affected_row = cursor.execute(
                    insert_product_images_query,
                    (product_id, image_id, is_main)
                )

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


    def select_color_list(self, db_connection):

        """

        상품의 색상 List를 Return 합니다.

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            product의 색상 List
            "data": [
                {
                    "color_no" : {color_no} ,
                    "name"     : "{color_nam}"
                }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성

        """

        with db_connection.cursor() as cursor:

            select_colors_query = """
            SELECT
                color_no,
                name

            FROM colors
            """

            cursor.execute(select_colors_query)
            colors = cursor.fetchall()

            return colors

    def select_size_list(self, db_connection):

        """

        상품의 사이즈 List를 Return 합니다.

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            product의 사이즈 List
            "data": [
                {
                    "size_no" : {size_no},
                    "name"    : "{size_name}"
                }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성

        """

        with db_connection.cursor() as cursor:

            select_colors_query = """
            SELECT
                size_no,
                name

            FROM sizes
            """

            cursor.execute(select_colors_query)
            colors = cursor.fetchall()

            return colors


    def insert_product_option(self, product_id, db_connection):

        """

       상품의 옵션 정보 테이블(product_options)에 insert 하고 product_option_no(PK)를 Return 합니다.

        Args:
            product_id    : 상품 테이블(products) PK
            db_connection : DATABASE Connection Instance

        Returns:
            product_option_no(PK)

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성

        """

        try:
            with db_connection.cursor() as cursor:

                insert_product_options_query = """
                INSERT INTO product_options (
                    product_id,
                    is_deleted
                ) VALUES (
                    %s,
                    DEFAULT
                )
                """

                affected_row = cursor.execute(insert_product_options_query, product_id)

                if affected_row <= 0 :
                    raise Exception('QUERY_FAILED')

                # 등록한 images 테이블의 row id Return
                return cursor.lastrowid

        except KeyError as e:
            raise e

        except Exception as e:
            raise e


    def insert_option_detail(self, product_option_id, option, db_connection):

        """

        옵션 상세 정보 테이블(option_details)에 insert 하고 option_details_no(PK)를 Return 합니다.

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            option_details_no(PK)

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성

        """

        try:
            with db_connection.cursor() as cursor:

                insert_option_details_query = """
                INSERT INTO option_details (
                    product_option_id,
                    color_id,
                    size_id
                ) VALUES (
                    %s,
                    %s,
                    %s
                )
                """

                #print(option)

                affected_row = cursor.execute(
                    insert_option_details_query,
                    (product_option_id, option['colorId'], option['sizeId'])
                )

                if affected_row <= 0 :
                    raise Exception('QUERY_FAILED')

                # 등록한 images 테이블의 row id Return
                return cursor.lastrowid

        except KeyError as e:
            raise e

        except Exception as e:
            raise e



    def insert_quantity(self, option_detail_id, option, db_connection):

        """

        상품 제고 수량 테이블(quantities)에 insert 합니다.

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            None

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-29 (sincerity410@gmail.com) : 초기생성

        """

        try:
            with db_connection.cursor() as cursor:

                insert_quantities_query = """
                INSERT INTO quantities (
                    option_detail_id,
                    quantity
                ) VALUES (
                    %s,
                    %s
                )
                """

                affected_row = cursor.execute(
                    insert_quantities_query,
                    (option_detail_id, option['quantity'])
                )

                if affected_row <= 0 :
                    raise Exception('QUERY_FAILED')

                # 등록한 images 테이블의 row id Return
                return None

        except KeyError as e:
            raise e

        except Exception as e:
            raise e

    def select_main_category_list(self, db_connection):

        """

        상품의 Main Category List를 Return 합니다.

        Args:
            db_connection : DATABASE Connection Instance

        Returns:
            product의 Main Category List
            "data": [
                {
                  "main_category_no" : {main_category_id},
                  "name"             : "{main_category_name}"
                }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-30 (sincerity410@gmail.com) : 초기생성

        """

        with db_connection.cursor() as cursor:

            select_main_categories_query = """
            SELECT
                main_category_no,
                name

            FROM main_categories
            """

            cursor.execute(select_main_categories_query)
            main_categories = cursor.fetchall()

            return main_categories

    def select_sub_category_list(self, main_cetegory_id, db_connection):

        """

        상품의 Sub Category List를 Return 합니다.

        Args:
            main_category_id : main_categories 테이블의 PK
            db_connection    : DATABASE Connection Instance

        Returns:
            product의 Sub Category List
            "data": [
                {
                  "name"            : "{sub_category_name}",
                  "sub_category_no" : {sub_category_no}
                }
            ]

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-30 (sincerity410@gmail.com) : 초기생성

        """

        with db_connection.cursor() as cursor:

            print(main_cetegory_id)
            select_sub_categories_query = """
            SELECT
                sub_category_no,
                name

            FROM sub_categories

            WHERE
                main_category_id = %s
            """

            cursor.execute(select_sub_categories_query, main_cetegory_id)
            sub_categories = cursor.fetchall()

            return sub_categories
