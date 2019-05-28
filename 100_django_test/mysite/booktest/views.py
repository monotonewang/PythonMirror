from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request,'booktest/views/hero_info.html',{'hero':bookinfo,'list':range(1,10)})
