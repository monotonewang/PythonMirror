from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import HeroInfo
from .models import BookInfo
from .models import EmpolyeeBasicInfo
from .models import EmpolyeeDetailInfo
from django.http import Http404
from django.shortcuts import get_object_or_404
from datetime import date
from django.db.models import Q
from django.db.models import F
from django.db.models import Sum, Count, Max, Min, Avg
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index2(request):
    return HttpResponse("index2")


def getHero(request, hero_id):
    #  return HttpResponse("getHero")
     try:
        hero = HeroInfo.objects.get(pk=hero_id)
     except HeroInfo.DoesNotExist:
        raise Http404("Hero does not exist")
     return render(request, 'booktest/views/hero_info.html', {'hero': hero})

# 这是上面getHero的简写


def getBook(request, book_id):
    list = [1, 2, 3, 4, 5, 6, 7, 8]
   #  判等
   #  bookinfo=BookInfo.objects.get(id__exact=book_id)
   # likes
    bookinfo = BookInfo.objects.get(btitle__contains='笑')
    # 以什么结尾
    bookinfo = BookInfo.objects.get(btitle__endswith='部')
    # 查看图书信息。要求图书关联英雄的名称包含 部
    bookinfo = BookInfo.objects.get(heroinfo_hname__contains='部')

   #  bookinfo = HeroInfo.objects.get(hbook_name='天龙八部')

   #  bookinfo=get_object_or_404(BookInfo,pk=book_id)
    return render(request, 'booktest/views/book_info.html', {'book': bookinfo, 'list': range(1, 10)})


def getBooks(request):
    bookinfo = BookInfo.objects.all()
   #  范围查询
    bookinfo = BookInfo.objects.filter(id__in=[1, 3])
   #  id大于2 gte 大于等于
    bookinfo = BookInfo.objects.filter(id__gt=2)
   #  id 小于 lte 小于等于
    bookinfo = BookInfo.objects.filter(id__lt=2)
   #  查询不为空的
    bookinfo = BookInfo.objects.filter(btitle__isnull=False)
   #  查询1月份的 书籍
    bookinfo = BookInfo.objects.filter(bpub_date__month=1)
   #  查询时间大于1980年1月1号的
    bookinfo = BookInfo.objects.filter(bpub_date__gt=date(1980, 1, 1))
   #  加了- 号 表示降序
    bookinfo = BookInfo.objects.all().order_by('-id')
   #  查询id不等于1 的书籍
   #  bookinfo=BookInfo.objects.exclude(id=1)
    bookinfo = BookInfo.objects.filter(id__gt=2).order_by('-bcomment')
    bookinfo = BookInfo.objects.filter(id__gt=2, bcomment__gt=30)
   #  表示并且的关系
    bookinfo = BookInfo.objects.filter((Q(id__gt=2)) & Q(bcomment__gt=30))
   #  F 用于类属性的比较
    bookinfo = BookInfo.objects.filter(bcomment__gt=F('bread')*2)
    bookinfo = BookInfo.objects.all()
    return render(request, 'booktest/views/book_infos.html', {'book': bookinfo, })


def getBookDetail(request, book_id):
   bookinfo = get_object_or_404(BookInfo, pk=book_id)
   hero = bookinfo.heroinfo_set.all()
   count = bookinfo.heroinfo_set.all().count()
   # 聚合
   count = bookinfo.heroinfo_set.all().aggregate(Count('id'))
   comment_count = bookinfo.heroinfo_set.all().aggregate(Sum('id'))
   print("count="+str(count)+"comment_count="+str(comment_count))

   return render(request, 'booktest/views/book_detail.html', {'hero': hero, 'bookinfo': bookinfo})


def add_hero(request, book_id):
   bookinfo = get_object_or_404(BookInfo, pk=book_id)
   obj = HeroInfo(hname='杨过', hcomment='黯然销魂掌', hbook=bookinfo)
   obj.save()
   # 原理等同于 HttpResponseRedirect
   return redirect('getBookDetail', book_id)


def delete_hero(request, hero_id, book_id):
   HeroInfo.objects.filter(id=hero_id).delete()
   return redirect('getBookDetail', book_id)

# 1对1的数据保存


def oneToOneSave(request):
   temp = "张三"
   ages = 1
   empoly = EmpolyeeBasicInfo(name=temp, age=ages)
   empoly.save()
   all = EmpolyeeBasicInfo.objects.all()
   allDetail = EmpolyeeDetailInfo(
       name=temp, age=ages, address="北京", empolyee_basic=empoly)
   allDetail.save()
   return HttpResponse(allDetail)

# 1对1删除会产生连锁反应， 一张表对应数据删除，然后其他数据就没有了


def oneToOneDelete(request):
   EmpolyeeBasicInfo.objects.filter(id=5).delete()
   allEmpoly = EmpolyeeDetailInfo.objects.all()
   return HttpResponse(allEmpoly)


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

#跳转到登录页面
def login(request):
    return render(request, 'booktest/views/login.html')

# 对应 input里面的 name 属性

#登录处理的action
def login_action(request):
    path = request.path
    method = request.method
    print("xxx path="+path+"method="+method)
    name=str(request.POST.get('username'))
    pwd=str(request.POST.get('password'))
    if(name=="python" and pwd=="python"):
        return redirect("getBooks")
    else:
        return redirect("/booktest/login")#重定向到登录了
      #   return redirect(request,'booktest/views/login.html')#重定向到登录了
   #  return HttpResponse("success"+"name="+name+"pwd="+pwd)
