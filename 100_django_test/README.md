 <!-- offical website -->
 https://www.djangoproject.com/

 <!-- check django version -->
 python3 -m django --version
 
 <!-- create project -->
 django-admin startproject mysite

<!-- change port -->
 python3 manage.py runserver 8080
 python3 manage.py runserver 192.168.1.101:8080

<!-- create your app -->
 python3 manage.py startapp booktest

<!-- 创建Django基本表 包括用户写的model -->
python3 manage.py migrate

<!-- 用于查看某个版本的迁移 sql语句 -->
python3 manage.py sqlmigrate booktest 0002

<!-- setting.py INSTALLED_APPS  注册 'booktest.apps.BookConfig'-->
<!-- Now Django knows to include the polls app. Let’s run another command: -->
python3 manage.py makemigrations booktest

<!-- 通过shell控制 -->
python manage.py shell

<!-- 开启后台控制功能 -->
python3 manage.py createsuperuser

<!-- 后台访问路径 -->
http://127.0.0.1:8080/admin/