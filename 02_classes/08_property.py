
# 使用property取代getter和setter方法
class Goods:

    @property
    def price(self):
        print("property")
        return 100

    @price.setter
    def price(self,value):
        print("setter")    

    @price.deleter
    def price(self):
        print("deleter")    


goods=Goods();

print(goods.price)
goods.price=100

del goods.price

print(goods.__dir__)