from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import HeroInfo
from .models import BookInfo
from django.http import Http404
from django.shortcuts import get_object_or_404

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
def getBook(request,book_id):
    list=[1,2,3,4,5,6,7,8]
    bookinfo=get_object_or_404(BookInfo,pk=book_id)
    return render(request,'booktest/views/book_info.html',{'book':bookinfo,'list':range(1,10)})

def getBooks(request):
    bookinfo=BookInfo.objects.all()
    return render(request,'booktest/views/book_infos.html',{'book':bookinfo,})

def getBookDetail(request,book_id):
   bookinfo=get_object_or_404(BookInfo,pk=book_id)
   hero=bookinfo.heroinfo_set.all()
   return render(request,'booktest/views/book_detail.html',{'hero':hero,'bookinfo':bookinfo})

def add_hero(request,book_id):
   bookinfo=get_object_or_404(BookInfo,pk=book_id)
   obj = HeroInfo(hname='杨过',hcomment='黯然销魂掌',hbook=bookinfo)
   obj.save()
   # 原理等同于 HttpResponseRedirect
   return redirect('getBookDetail',book_id)

def delete_hero(request,hero_id,book_id):
   HeroInfo.objects.filter(id=hero_id).delete()
   return redirect('getBookDetail',book_id)