from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_titile=models.DateField()
    # 阅读量
    bread=models.IntegerField(default=0)
    # 评论量
    bcomment=models.IntegerField(default=0)
    # 删除标记
    bdelete=models.BooleanField(default=False)

    def __str__(self):
        return self.btitle+ "-->title="+str(self.bpub_titile);

class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField(default=False)
    hcomment=models.CharField(max_length=128)
    # 一对多关系
    hbook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    hdelete=models.BooleanField(default=False)
    def __str__(self):
        return self.hname+ "-->="+str(self.hcomment)+str(self.hbook);