from pymysql import connect

connect = connect(host="localhost", port=3306, user="root",
                  password="Ab123456", database="jing_dong")
# create cursor object
cursor = connect.cursor()

temp_name="'' or 1=1"

# 错误用法2：
sql = "select * from goods_cate where name=" +temp_name 

# select * from goods_cate where name='' or 1=1;

cursor.execute(sql)

for temp in cursor.fetchall():
        print(temp)


print("right way to do")

# 正确用法1： 使用‘’or 1=1 无法查询到数据
args = (temp_name)
# args = ("Pad")

sql = "select * from goods_cate where name=%s"

cursor.execute(sql, args)

for temp in cursor.fetchall():
        print(temp)

cursor.close()
connect.close()