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

        """

        try:
            with db_connection.cursor() as cursor:

                insert_product_query = """
                INSERT INTO products (
                    created_at,
                    is_deleted
                ) VALUES (
                    DEFAULT,
                    DEFAULT
                    )
                """

                affected_row = cursor.execute(insert_product_query)

                if affected_row == -1:
                    raise Exception('QUERY_FAILED')

                return cursor.lastrowid

        except Exception as e:
            raise e

    def insert_product_detail(self, product_info, db_connection):

        """

        상품등록 Model Function

        Args:
            product_info  : ProductService.create_product로 받은 Parameter
            db_connection : DATABASE Connection Instance

        Returns:
            200: SUCCESS, (상품등록 완료)

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-25 (sincerity410@gmail.com) : 초기생성

        """

        try:
            with db_connection.cursor() as cursor:

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

                affected_row = cursor.execute(insert_product_detail_query, product_info)

                if affected_row == -1:
                    raise Exception('QUERY_FAILED')

                return cursor.lastrowid

        except Exception as e:
            raise e

        return jsonify({'message' : 'SUCCESS'}), 200

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
