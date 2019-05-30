from django.db import models

# Create your models here.
#图书模型管理器类


class BookInfoManager(models.Manager):
    # 1.改变查询的结果集 获取到的books 对 isDelete进行过滤
    def all(self):
        # 对数据进行过滤
        books = super().all()
        books = books.filter(isDelete=False)
        return books
    #2.封装函数（增删改查）创建book对象 可以通过类名调用类方法直接完成报错对象操作

    def create_book(self,btitle, b_pub_date):
        # 第一种
        # obj = BookInfo()
        # 第二种创建方式
        model_class=self.model
        obj=model_class()

        obj.btitle = btitle
        obj.b_pub_date = b_pub_date
        obj.save()
        return obj
    pass


class BookInfo(models.Model):
    # 唯一 索引
    btitle = models.CharField(max_length=20, unique=True, db_index=True)
    # 发布时间 dbcolumn 表字段名称
    bpub_date = models.DateField(
        auto_now=False, auto_now_add=True, db_column="b_pub_date")
    # 阅读量
    bread = models.IntegerField(default=0)
    # 图书价格 最大位数10 小数点后面2位 DecimalField需要一个default参数
    bprice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    bdelete = models.BooleanField(default=False)

    # 自定义管理器对象
    # 第一种写法
    # books=models.Model() 查询 BookInfo.books.all()
    # 第二种写法
    # objects=BookInfoManager()
    # BookInfo.objects.all()
    #2.封装函数（增删改查）创建book对象 可以通过类名调用类方法直接完成报错对象操作
    @classmethod
    def create_book(cls, btitle, b_pub_date):
        obj = cls()
        obj.btitle = btitle
        obj.b_pub_date = b_pub_date
        obj.save()
        return obj
    # objects.create_book("x",(1980,1,1))

    def __str__(self):
        return self.btitle + "-->title="+str(self.bpub_date)

    # 元选项-->项目名和数据库是一致的
    # class Meta:
    #     db_table='bookinfo'#制定模型类的表名 重新迁移（表名会发生变化）


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    # Null 是否为空 blank控制后台管理系统是否可以空白输入
    hcomment = models.CharField(max_length=128, null=True, blank=False)
    # 一对多关系
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    hdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname + "-->="+str(self.hcomment)+str(self.hbook)

# 新闻类型类


class NewsType(models.Model):
    type_name = models.CharField(max_length=20)
    # 多对多
    # type_news=models.ManyToManyField('News')

# 新闻类


class News(models.Model):
    title = models.CharField(max_length=20, unique=True)
    pub_date = models.DateField(auto_now=False, auto_now_add=True)
    comment = models.TextField()
    # 多对多
    news_type = models.ManyToManyField('NewsType')

    # 员工基本信息类


class EmpolyeeBasicInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
   # 一对一
    # empolyee_detail=models.ManyToManyField('EmpolyeeDetailInfo')


class EmpolyeeDetailInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()

    address = models.CharField(max_length=256)
    # 一对一
    empolyee_basic = models.OneToOneField(
        'EmpolyeeBasicInfo', on_delete=models.CASCADE)

# 自关联


class AreaInfo(models.Model):
    # 地区名称
    atitile = models.CharField(max_length=20)
    # 自关联是特殊的一对多 关联自己
    models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
