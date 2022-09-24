"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
=======
from django.urls import path, re_path
>>>>>>> db6a24b (Initial commit)
from firstapp import views


urlpatterns = [
<<<<<<< HEAD
    path('', admin.site.urls, name = 'home'),
    path('admin/', admin.site.urls),
=======
    path('', views.index, name = 'home'),
#    path('admin/', admin.site.urls),
    #path('about', views.about, name = 'about'),
    re_path(r'^about', views.about, name = 'about'),
    re_path(r'^contact', views.contact, name = 'contact'),
    #re_path(r'^users/(?P<id>\d+)/(?P<user_name>\D+)', views.users),
    path('users/<int:id>/<str:user_name>/', views.users),
    path('users/', views.users), # по умолчанию
    path ('products/<int:id>/<str:user_name>', views.products),
    path ('products/', views.products), # по умолчанию
    #path ('home/', views.home),

    #re_path(r'^users/$', views.users), # маршрут по умолчанию для явно незаданного юзера
    #re_path(r'^products/$', views.products), # маршрут по умолчанию для явно незаданной продукции
    #re_path(r'^products/(?P<product_id>\d+)', views.products),

>>>>>>> db6a24b (Initial commit)
]
