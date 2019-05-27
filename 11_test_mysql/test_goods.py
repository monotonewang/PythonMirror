# -*- coding: utf-8 -*-
from pymysql import connect
import platform
import sys
import time


class Goods():
    def __init__(self, password):
        # 创建 connection对象
        self.connect = None
        self.cursor = None
        try:
            self.connect = connect(host="localhost", port=3306, user="root",
                                   password=password, database="jing_dong")
            # create cursor object
            self.cursor = self.connect.cursor()
        except:
            print("get error exception")
            pass

    def show_all_item(self):
        # if(hasattr(self,"cursor")):
        if(self.cursor is not None):
            print("yes attribute")
            count = self.cursor.execute("select * from goods;")
            print("good all count %d" % count)
            for temp in self.cursor.fetchall():
                print(temp)
        else:
            print("no attribute")

    def show_cate(self):
        count = self.cursor.execute(
            "select g.name,gc.name from goods as g inner join goods_cate as gc  where g.cate_name=gc.id;")
        print("cate all count %d" % count)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_brand(self):
        count = self.cursor.execute(
            "select * from goods_cate")
        print("cate all count %d" % count)
        for temp in self.cursor.fetchall():
            print(temp)

    # 一次性插入10万条数据
    def insert_goods(self):
        start_time=time.time()
        try:
            for i in range(0,100000):
                title='15.6寸笔记本='+str(i)
                count = self.cursor.execute(
                    "insert into goods values(0, %s,'笔记本','华硕',3329,default,default);",title)
                print("insert_goods %d %s" % (count,title));
            self.connect.commit()
            end_time=time.time()
            print("经历时间 %f" % (end_time-start_time));
        except Exception as s:
            print(s)
            self.connect.rollback();
        
    def __delete__(self):
        self.cursor.close()
        self.connect.close()

    def run(self):
        print(platform.python_version())
        print(sys.version)
        print(sys.version_info)
        i = 1
        while i == 1 or i == 2 or i == 3:
            print(u'1.所有商品')
            print("2.商品分类")
            print("3.商品品牌分类")
            i = input("please 数字")
            try:
                i = int(i)
                if i == 1:
                    self.show_all_item()
                elif (i == 2):
                    self.show_cate()
                elif (i == 3):
                    self.show_brand()
                else:
                    print("input error")
                    time.sleep(2)  # 延迟执行
                    print("exit")
                    break

            except Exception as result:
                print("run Exception result %s" % result)
                pass


if __name__ == "__main__":
    goods = Goods("Ab123456")
    goods.insert_goods()
    # goods.run()
    pass
