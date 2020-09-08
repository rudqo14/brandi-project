import uuid

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
            2020-09-02 (sincerity410@gmail.com) : product_code 등록 추가

        """

        try:
            with db_connection.cursor() as cursor:

                # insert new product
                insert_product_query = """
                INSERT INTO products (
                    created_at,
                    is_deleted,
                    product_code
                ) VALUES (
                    DEFAULT,
                    DEFAULT,
                    %s
                    )
                """

                # insert query execute
                affected_row = cursor.execute(insert_product_query, str(uuid.uuid4()))

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
            2020-08-28 (minho.lee0716@gmail.com) : 수정
                Image 테이블 필드명을 나누어 image > image_medium으로 바꿈
            2020-09-01 (minho.lee0716@gmail.com) : 수정
                상품을 최신 등록순으로 보여주기 위해 내림차순(DESC)으로 정렬
            2020-09-04 (tnwjd060124@gmail.com) : 수정
                현재 이력 조회 조건 변경
            2020-09-05 (tnwjd060124@gmail.com) : 수정
                할인 기간에 따른 할인률 조회 조건 추가

        """

        with db_connection.cursor() as cursor:

            select_products_query = """
            SELECT
                P.product_no,
                I.image_medium AS thumbnail_image,
                PD.name AS product_name,
                PD.price AS original_price,
                CASE
                    WHEN PD.discount_rate IS NULL THEN 0 -- discount_rate이 NULL 인 경우 0
                    ELSE CASE
                        WHEN PD.discount_start_date IS NULL THEN PD.discount_rate -- 할인 기간이 무기한인 경우
                        WHEN NOW() BETWEEN PD.discount_start_date AND PD.discount_end_date THEN PD.discount_rate -- 할인기간이 유효한 경우
                        ELSE 0 -- 할인 기간이 아닌 경우
                        END
                    END
                AS discount_rate

            FROM products AS P

            INNER JOIN product_images as PI
            ON P.product_no = PI.product_id
            AND PI.close_time = '9999-12-31 23:59:59'
            AND PI.is_main = 1

            INNER JOIN images as I
            ON PI.image_id = I.image_no
            AND I.is_deleted = 0

            INNER JOIN product_details as PD
            ON P.product_no = PD.product_id
            AND PD.is_activated = 1
            AND PD.is_displayed = 1
            AND PD.close_time = '9999-12-31 23:59:59'

            WHERE
                P.is_deleted = False

            ORDER BY
                P.product_no DESC;
            """

            # 상품을 등록하고, row를 고려해 전체 리스트에서는 상품 id의 역순으로 리턴해줍니다.

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
            2020-08-30 (minho.lee0716@gmail.com) : 현재 이력만 조회하는 조건 추가
            2020-08-31 (minho.lee0716@gmail.com) : 키값 수정
                detail_information > html,
                product_no > product_id
            2020-09-04 (tnwjd060124@gmail.com) : 수정
                현재 이력 조회 조건 변경
            2020-09-05 (tnwjd060124@gmail.com) : 수정
                할인 기간에 유효한 조건 조회 변경

        """

        with db_connection.cursor() as cursor:

            select_product_details_query = """
            SELECT
                P.product_no AS product_id,
                PD.name,
                PD.detail_information AS html,
                PD.price AS original_price,
                PD.min_sales_quantity,
                PD.max_sales_quantity,
                CASE
                    WHEN PD.discount_rate IS NULL THEN 0
                    ELSE CASE
                        WHEN PD.discount_start_date IS NULL THEN PD.discount_rate
                        WHEN NOW() BETWEEN PD.discount_start_date AND PD.discount_end_date THEN PD.discount_rate
                        ELSE 0
                        END
                    END
                AS discount_rate

            FROM products AS P

            INNER JOIN product_details AS PD
            ON P.product_no = PD.product_id
            AND PD.is_activated = 1
            AND PD.is_displayed = 1
            AND PD.close_time = '9999-12-31 23:59:59'

            WHERE
                P.is_deleted = 0
                AND P.product_no = %s;
            """

            # 데이터들을 가져온 후, product_details라는 변수에 담아 리턴해줍니다.
            cursor.execute(select_product_details_query, product_id)
            product_details = cursor.fetchone()

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

                affected_row = cursor.execute(
                    insert_option_details_query,
                    (product_option_id, option['color_id'], option['size_id'])
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

    def select_product_images(self, product_id, db_connection):

        """

        상품 상세정보의 이미지들을 리턴합니다.

        Args:
            product_id    : 해당 상품의 id
            db_connection : 연결된 db 객체

        Returns:
            해당 상품에 대한 상세정보 이미지들

        Authors:
            minho.lee0716@gmail.com (이민호)
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-27 (minho.lee0716@gmail.com) : 초기 생성
            2020-08-31 (minho.lee0716@gmail.com) : 현재 이력만 조회하는 조건 추가
            2020-09-04 (tnwjd060124@gmail.com) : 현재 이력 조회하는 조건 수정

        """

        with db_connection.cursor() as cursor:

            select_product_images_query = """
            SELECT
                I.image_large

            FROM products AS P

            LEFT JOIN product_images AS PI
            ON P.product_no = PI.product_id
            AND PI.close_time = '9999-12-31 23:59:59'

            LEFT JOIN images AS I
            ON PI.image_id = I.image_no
            AND I.is_deleted = False

            WHERE
                P.product_no = %s
                AND P.is_deleted = False

            ORDER BY
                I.image_no ASC;
            """

            # 이미지를 순서대로(이미지 id의 오름차순) 정렬해줍니다

            # 데이터들을 가져온 후, product_images라는 변수에 담은 후,
            cursor.execute(select_product_images_query, product_id)
            product_images = cursor.fetchall()

            # 최종적으로 프론트에게 배열로 사진들을 주기 위헤 images라는 배열에 담습니다.
            images = [
                element['image_large']
            for element in product_images]

            return images

    def select_product_option_colors(self, product_id, db_connection):

        """

        서비스 페이지의 상품 상세정보중 컬러들을 리턴합니다.

        Args:
            product_id    : 해당 상품의 id
            db_connection : 연결된 db 객체

        Returns:
            해당 상품에 대한 상세정보의 옵션중 컬러들만 리턴.

        Authors:
            minho.lee0716@gmail.com (이민호)
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-30 (minho.lee0716@gmail.com) : 초기 생성
            2020-08-31 (minho.lee0716@gmail.com) : 현재 이력만 조회하는 조건 추가
            2020-08-31 (minho.lee0716@gmail.com) : 옵션 전체가 아닌, 컬러만 조회하기
            2020-09-04 (tnwjd060124@gmail.com)   : 현재 이력만 조회하는 조건 변경

        """

        with db_connection.cursor() as cursor:

            select_product_options_query = """
            SELECT DISTINCT
                C.color_no AS color_id,
                C.name AS color_name

            FROM products AS P

            LEFT JOIN product_options AS PO
            ON P.product_no = PO.product_id
            AND PO.is_deleted = False

            LEFT JOIN colors AS C
            ON PO.color_id = C.color_no

            WHERE
                P.product_no = %s
                AND P.is_deleted = False

            ORDER BY
                color_id ASC;
            """

            # color_id를 오름차순으로 정렬해줍니다.

            # 가져온 데이터들을 product_details라는 변수에 담은 후,
            cursor.execute(select_product_options_query, product_id)
            colors = cursor.fetchall()

            return colors

    def select_etc_options(self, product_info, db_connection):

        """

        서비스 페이지의 상품 상세정보중 사이즈와 수량을 리턴합니다.

        Args:
            product_info : {
                product_id    : 해당 상품의 id
                color_name    : 해당 상품의 color의 이름
            }
            db_connection : 연결된 db 객체

        Returns:
            해당 상품에 대한 상세정보의 옵션중 사이즈와 수량을 리턴

        Authors:
            minho.lee0716@gmail.com (이민호)
            tnwjd060124@gmail.com (손수정)

        History:
            2020-08-31 (minho.lee0716@gmail.com) : 초기 생성
            2020-09-01 (minho.lee0716@gmail.com) : 상품의 id에서 이름을 받는걸로 변경
            2020-09-01 (minho.lee0716@gmail.com) : 수정
                DB에서 데이터의 순서에 의해, 마지막에 역순으로 정렬
            2020-09-04 (tnwjd060124@gmail.com) : 수정
                현재 이력만 조회하는 조건 수정

        """

        with db_connection.cursor() as cursor:

            select_product_etc_options_query = """
            SELECT
                S.name AS size,
                S.size_no AS size_id,
                Q.quantity

            FROM products AS P

            LEFT JOIN product_options AS PO
            ON P.product_no = PO.product_id
            AND PO.is_deleted = False

            LEFT JOIN colors AS C
            ON PO.color_id = C.color_no

            LEFT JOIN sizes AS S
            ON PO.size_id = S.size_no

            LEFT JOIN quantities AS Q
            ON PO.product_option_no = Q.product_option_id
            AND Q.close_time = '9999-12-31 23:59:59'

            WHERE
                P.product_no = %(product_id)s
                AND P.is_deleted = False
                AND C.color_no = %(color_id)s

            ORDER BY
                S.size_no DESC;
            """

            # 사이즈는 큰 순서로 넣어줬기 때문에 역순으로 정렬하였습니다.

            # 불러온 데이터를 etc_options 라는 변수에 담아온 후, 리턴을 해줍니다.
            cursor.execute(select_product_etc_options_query, product_info)
            etc_options = cursor.fetchall()

            return etc_options

    def select_registered_product_list(self, filter_info, db_connection):

        """

        [상품관리 > 상품관리]
        관리자 페이지에서 등록된 상품의 List와 Total Count를 Return 합니다.

        Args:
            filter_info   : Parameter로 들어온 filter의 Dictionary 객체
            db_connection : DATABASE Connection Instance

        Returns:
            data: [
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

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-01 (sincerity410@gmail.com) : 초기생성
            2020-09-03 (sincerity410@gmail.com) : Filtering 조건 추가

        """

        with db_connection.cursor() as cursor:

            select_product_list_query = """
            -- 상품 조회 Query Start
            SELECT
                SQL_CALC_FOUND_ROWS
                P.created_at as productRegistDate,
                I.image_small as productSmallImageUrl,
                PD.name as productName,
                P.product_no as productNo,
                P.product_code as productCode,
                ROUND(PD.price, -1) as sellPrice,
                discountRate,
                ROUND(PD.price * (100-discountRate)/100, -1) AS discountPrice,
                CASE
                    WHEN discountRate = 0
                        THEN "미할인"
                    ELSE "할인"
                END AS discountYn,
                IF(PD.is_displayed = 1, "진열", "미진열") as productExhibitYn,
                IF(PD.is_activated = 1, "판매", "미판매") as productSellYn

            FROM (
                SELECT products.*,
                CASE
                	WHEN (product_details.discount_end_date IS NULL AND product_details.discount_start_date IS NULL) AND product_details.discount_rate IS NOT NULL
                		THEN product_details.discount_rate
                	WHEN (product_details.discount_end_date IS NOT NULL AND product_details.discount_start_date IS NOT NULL) AND (product_details.discount_start_date <= now() AND product_details.discount_end_date >= now())
                		THEN product_details.discount_rate
                	ELSE 0
                END AS discountRate
                FROM products

            INNER JOIN product_details
            ON product_details.product_id = products.product_no
            ) AS P

            INNER JOIN product_images as PI
            ON P.product_no = PI.product_id

            INNER JOIN images as I
            ON PI.image_id = I.image_no

            INNER JOIN product_details as PD
            ON PD.product_id = P.product_no

            WHERE
                PI.is_main = 1
                AND PI.close_time > now()
                AND PD.close_time > now()

            """

            # Filtering 시작

            # 판매 여부 필터링
            if filter_info['sellYn'] is not None :
                select_product_list_query += """
                AND PD.is_activated = %(sellYn)s
                """

            # 할인 여부 필터링
            if filter_info['discountYn'] is not None :
                select_product_list_query += """
                AND (
                CASE
                    WHEN discountRate = 0
                        THEN FALSE
                    ELSE TRUE
                END) = %(discountYn)s
                """

            # 진열 여부 필터링
            if filter_info['exhibitionYn'] is not None :
                select_product_list_query += """
                AND PD.is_displayed = %(exhibitionYn)s
                """

            # 상품 등록 기간 시작일자 필터링
            if filter_info['startDate'] is not None :
                select_product_list_query += """
                AND P.created_at >= %(startDate)s
                """

            # 상품 등록 기간 종료일자 필터링
            if filter_info['endDate'] is not None :
                filter_info['endDate'] += 1
                select_product_list_query += """
                AND P.created_at < %(endDate)s
                """

            # 상품명 일부 일치 조건 필터링
            if filter_info['productName'] is not None :
                filter_info['productName'] = f"%{filter_info['productName']}%"
                select_product_list_query += """
                AND PD.name like %(productName)s
                """

            # 상품 번호 일치 조건 필터링
            if filter_info['productNo'] is not None :
                select_product_list_query += """
                AND P.product_no = %(productNo)s
                """

            # 상품 코드 일치 조건 필터링
            if filter_info['productCode'] is not None :
                select_product_list_query += """
                AND P.product_code = %(productCode)s
                """

            # 정렬 및 Page Nation 적용
            select_product_list_query += """
            ORDER BY
                P.product_no DESC

            LIMIT
                %(limit)s
            OFFSET
                %(offset)s
            """

            cursor.execute(select_product_list_query, filter_info)
            product_list = cursor.fetchall()

            select_product_count = """
            SELECT FOUND_ROWS() as total
            """

            cursor.execute(select_product_count)
            total = cursor.fetchone()

            return product_list, total

    def select_product_code(self, product_id, db_connection):

        """

        상품 테이블(products)의 product_code 값을 Return 합니다.

        Args:
            product_id : products 테이블의 PK
            db_connection : DATABASE Connection Instance

        Returns:
            product_code : products Table의 product_code(Unique Value)

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-02 (sincerity410@gmail.com) : 초기생성

        """

        with db_connection.cursor() as cursor:

            select_product_code_query = """
            SELECT
                product_code

            FROM products

            WHERE
                product_no = %s
            """

            cursor.execute(select_product_code_query, product_id)
            product_code = cursor.fetchone()

            return product_code

    def select_color_id(self, option, db_connection):

        """

        option Dictionary 객체의 colorName으로 부터 color id(PK)를 Return 합니다.

        Args:
            option        : product regist의 optionQuantity key의 value
            db_connection : DATABASE Connection Instance

        Returns:
            color_no : colors table PK

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-05 (sincerity410@gmail.com) : 초기생성

        """

        with db_connection.cursor() as cursor:

            select_color_id_query = """
            SELECT
                color_no

            FROM colors

            WHERE
                name = %s
            """

            cursor.execute(select_color_id_query, option['color'])
            color_id = cursor.fetchone()

            return color_id['color_no']

    def select_size_id(self, option, db_connection):

        """

        option Dictionary 객체의 sizeName으로 부터 size id(PK)를 Return 합니다.

        Args:
            option        : product regist의 optionQuantity key의 value
            db_connection : DATABASE Connection Instance

        Returns:
            size_no : sizes table PK

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-09-05 (sincerity410@gmail.com) : 초기생성

        """

        with db_connection.cursor() as cursor:

            select_size_id_query = """
            SELECT
                size_no

            FROM sizes

            WHERE
                name = %s
            """

            cursor.execute(select_size_id_query, option['size'])
            size_id = cursor.fetchone()

            return size_id['size_no']

