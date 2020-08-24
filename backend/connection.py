import pymysql

from config import DATABASE

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

    return pymysql.connect(
        host        = DATABASE["host"],
        port        = DATABASE["port"],
        user        = DATABASE["user"],
        password    = DATABASE["password"],
        database    = DATABASE["database"],
        charset     = DATABASE["charset"],
        cursorclass = pymysql.cursors.DictCursor
    )

