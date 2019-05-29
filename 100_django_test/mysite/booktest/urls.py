from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),

    # http://localhost:8080/booktest/getHero/1
    # 后面的name是给html使用的
    path('getHero/<int:hero_id>', views.getHero, name='getHero'),
    path('getBook/<int:book_id>', views.getBook, name='getBook'),
    path('getBooks', views.getBooks, name='getBooks'),
    path('books/<int:book_id>', views.getBookDetail, name='getBookDetail'),
    path('add_hero/<int:book_id>', views.add_hero, name='add_hero'),
    path('delete_hero/<int:hero_id>/<int:book_id>', views.delete_hero, name='view_delete_hero'),
]