class Dao:

    def get_start_time(self, data, db_connection):

        """

        원하는 정보의 start_time을 리턴합니다.

        Args:
            data:
                table_name : 테이블 이름
                table_column : 조건으로 주는 colunm 명
                info : 조건

        Returns:
            start_time : 이력 시작 시간

        Author:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-09-07 (tnwjd060124@gmail.com) : 초기 생성

        """

        with db_connection.cursor() as cursor:
            get_start_time = """
            SELECT
                start_time
            FROM
                %(table_name)s
            WHERE
                %(table_column)s = %(info)s
            """

            cursor.execute(get_start_time, data)

            return cursor.fetchone()

    def get_original_info(self, data, db_connection):

        """

        원하는 정보의 현재 유효한 이력을 리턴합니다.

        Args:
            data:
                select_table_column : 원하는 table의 pk column 명
                table_name : 테이블 이름
                table_column : 조건으로 주는 column 명
                info : 조건

        Returns:
            no : 현재 유효한 이력의 pk

        Author:
            tnwjd060124@gmail.com (손수정)

        History:
            2020-09-07 (tnwjd060124@gmail.com) : 초기 생성

        """

        with db_connection.cursor() as cursor:
            get_original_no = """
            SELECT
                %(select_table_column)s
            FROM
                %(table_name)s
            WHERE
                %(table_column)s = %(info)s
                AND close_time = '9999-12-31 23:59:59'
            """

            cursor.execute(get_original_no, data)

            return cursor.fetchone()
