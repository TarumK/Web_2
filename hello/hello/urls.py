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
from django.urls import path
from django.urls import path, re_path
from firstapp import views
from django.views.generic import TemplateView


urlpatterns = [

    # path('', admin.site.urls, name = 'home'),
    path('search/', views.search),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create/', views.create),
    path('delete/<int:id>/', views.delete),
    path('edit/<int:id>/', views.edit),
    #path('admin/', admin.site.urls),
    #path('about', views.about, name = 'about'),
    # re_path(r'^about', views.about, name = 'about'),
    # re_path(r'^contact', views.contact, name = 'contact'),
    path('about', TemplateView.as_view(template_name="firstapp/about.html")),
    path('contact', TemplateView.as_view(template_name="firstapp/contact.html", extra_context={"work": "Отдел закупок"})),
    #re_path(r'^users/(?P<id>\d+)/(?P<user_name>\D+)', views.users),
    path('users/<int:id>/<str:user_name>/', views.users),
    path('users/', views.users), # по умолчанию
    path('products/<int:id>/<str:user_name>', views.products),
    path('products/', views.products), # по умолчанию
    #path('home/', views.home),

    #re_path(r'^users/$', views.users), # маршрут по умолчанию для явно незаданного юзера
    #re_path(r'^products/$', views.products), # маршрут по умолчанию для явно незаданной продукции
    #re_path(r'^products/(?P<product_id>\d+)', views.products),


]
