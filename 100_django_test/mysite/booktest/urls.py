from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

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
    path('oneToOneSave', views.oneToOneSave, name='oneToOneSave'),
    path('oneToOneDelete', views.oneToOneDelete, name='oneToOneDelete'),
    path('login', views.login, name='login'),
    path('login_action', views.login_action, name='login_action'),
    path('template_extend', views.template_extend, name='template_extend'),
    path('ajax_handle', views.ajax_handle, name='ajax_handle'),
    path('book_list', views.book_list, name='book_list'),
    
    # path(r'^showarg(\d+)$', views.showarg, name='showarg'),
    
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


handler404 = 'booktest.views.handler404'
handler500 = 'booktest.views.handler500'