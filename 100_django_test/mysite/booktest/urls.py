from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),

    # http://localhost:8080/booktest/getHero/1
    path('getHero/<int:hero_id>', views.getHero, name='getHero'),
    path('getBook/<int:book_id>', views.getBook, name='getBook'),
]