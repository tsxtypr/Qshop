from . import views
from django.urls import path,re_path

urlpatterns = [
    path('login/',views.login),
    path('index/',views.index),
    path('register/',views.register),
    path('user_center_info/',views.user_center_info),
    path('base/',views.base),
    path('index/',views.index),
    path('logout/',views.logout),
    re_path('goods_list/(?P<page>\d+)/',views.goods_list),
    path('detail_info/',views.detail_info),
    path('pay/',views.pay),
    path('alipayviews/',views.AlipayViews),
    path('payresult/',views.payresult),
]