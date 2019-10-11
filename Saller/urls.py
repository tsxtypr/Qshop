"""DjangoLogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include,re_path
from Saller import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
    path('base/', views.base),
    path('goods_list/', views.goods_list),
    re_path('goods_list/(?P<type>\d+)/(?P<page>\d+)/', views.goods_list),
    re_path('setstatus/(?P<status>\w+)/(?P<id>\d+)/', views.setstatus),
    path('personal_info/', views.personal_info),
    path('add_data/', views.add_data),
    path('update_data/', views.update_data),
    re_path('order_info/(?P<status>\d+)/', views.order_info),

]


