from flask import jsonify

class ProductDao:

    def insert_product(self, product_info, db_connection):
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

        cursor = db_connection.cursor()
        insert_product = """
            INSERT INTO products (
                created_at,
                is_deleted
                ) VALUES (
                DEFAULT,
                DEFAULT
                );
        """
        cursor.execute(insert_product)
        product_info['product_id'] = cursor.lastrowid

        insert_product_detail = """
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
        cursor.execute(insert_product_detail, product_info)
        db_connection.commit()

        return jsonify({'message' : 'SUCCESS'}), 200
