# -*- coding: utf-8 -*-
from pymysql import connect
import platform
import sys
import time

def noTransation():
    conn = connect(host="localhost", port=3306, user="root",
                    password="Ab123456", database="jing_dong")
    # create cursor object
    cursor = conn.cursor()
    cursor.execute("update goods set price=200 where id=1;")
    # cursor.execute("update goods set price=test where id=2;")

    #  提交之前，如果进行过 execute 就需要使用commit
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    noTransation()
    pass