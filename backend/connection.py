import pymysql, boto3

from config import DATABASE
from config import S3

def get_connection():
    """

    import 되어서 사용될 때마다 connection 생성

    Returns :
        database connection 객체

    Authors :
        tnwjd060124@gmail.com (손수정)

    History :
        2020-08-19 (tnwjd060124@gmail.com) : 초기 생성

    """

    connection = pymysql.connect(
        host        = DATABASE["host"],
        port        = DATABASE["port"],
        user        = DATABASE["user"],
        password    = DATABASE["password"],
        database    = DATABASE["database"],
        charset     = DATABASE["charset"],
        cursorclass = pymysql.cursors.DictCursor
    )
    connection.cursor().execute("""SET time_zone='Asia/Seoul'""")

    return connection

def get_s3_connection():
    s3_connection = boto3.client(
        's3',
        aws_access_key_id     = S3['aws_access_key_id'],
        aws_secret_access_key = S3['aws_secret_access_key']
    )

    return s3_connection

