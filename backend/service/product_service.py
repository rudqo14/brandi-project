from model.product_dao import ProductDao

class ProductService:
    def create_product(self, product_info, db_connection):
        """
        상품등록 Service function
        Args:
            product_info  : AdminProductView.product_register로 받은 Parameter
            db_connection : DATABASE Connection Instance

        Returns:
            200: SUCCESS, (상품등록 완료)

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-25 (sincerity410@gmail.com) : 초기생성
        """

        product_dao           = ProductDao()
        product_create_result = product_dao.insert_product(product_info, db_connection)

        return product_create_result
