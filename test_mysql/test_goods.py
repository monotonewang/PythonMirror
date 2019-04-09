# -*- coding: utf-8 -*-?
from pymysql import connect
import platform
import sys

class Goods():
    def __init__(self):
        # ?? connection???
        self.connect = connect(host="localhost", port=3306, user="root",
                          password="Ab123456", database="jing_dong")
        # ?? cursor??
        self.cursor = self.connect.cursor()

    def show_all_item(self):
        count = self.cursor.execute("select * from goods;")
        print("xxxxxx count %d" % count)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_cate(self):
        count = self.cursor.execute(
            "select g.name,gc.name from goods as g inner join goods_cate as gc  where g.cate_name=gc.id;")
        print("xxxxxx count %d" % count)
        for temp in self.cursor.fetchall():
            print(temp)

    def __delete__(self):
        self.cursor.close()
        self.connect.close()

    def run(self):
        print(platform.python_version())
        print(sys.version)
        print(sys.version_info)
        i=1
        while i==1 or i==2 or i==3:
            print(u'1.????')
            print("2.??????")
            print("3.????????")
            i=input("please ?????????")
            i=int(i)
            if i==1:
              self.show_all_item();
            else :
              self.show_cate();



if __name__ == "__main__":
    goods=Goods();
    goods.run();
    pass

