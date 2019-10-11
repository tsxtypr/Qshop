from django.db import models
from Saller.models import *

# 订单表
ORDER_LIST = (
    (0,'未支付'),
    (1,'已支付'),
    (2,'待发货'),
    (3,'待收货'),
    (4,'完成'),
    (5,'拒收'),
)
class PayOrder(models.Model):
    # 订单状态
    # 0  未支付
    # 1  已支付
    # 2 待发货
    # 3 待收货
    # 4 完成
    # 5  拒收
    order_number=models.CharField(max_length=32,verbose_name="订单编号",unique=True)
    order_date=models.DateField(auto_now=True,verbose_name="订单日期")
    order_status=models.IntegerField(choices=ORDER_LIST,verbose_name="订单状态")
    order_total=models.FloatField(verbose_name="订单总价")
    # 外键
    order_user=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)

# 订单信息表
class OrderInfo(models.Model):
    order_id=models.ForeignKey(to=PayOrder,on_delete=models.CASCADE,verbose_name="订单表")
    good_id=models.ForeignKey(to=Goods,on_delete=models.CASCADE,verbose_name="商品表")
    goods_count=models.IntegerField(verbose_name="商品数量")
    goods_tatol_price=models.FloatField(verbose_name="商品小计")
    store_id=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name="店铺id")
    goods_price=models.FloatField(default=10)
    orderinfo_status=models.IntegerField(choices=ORDER_LIST,verbose_name="订单状态",default=0)

class Cart(models.Model):
    goods_number=models.IntegerField(verbose_name="商品数量")
    goods_price=models.FloatField(verbose_name="商品单价")
    goods_total=models.FloatField(verbose_name="商品总价")
    goods=models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    cart_user=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)
    # 订单状态
    # 0  未支付
    # 1  已支付
    # 2 待发货
    # 3 待收货
    # 4 完成
    # 5  拒收
    status=models.IntegerField(verbose_name="订单状态",default=0)
    number=models.CharField(max_length=32,verbose_name="订单编号",default="0")

addr_status=(
    (1,"默认地址"),
    (2,'非默认地址')
)
class RecAddress(models.Model):
    username=models.CharField(max_length=10,verbose_name="收件人")
    detail_addr=models.TextField(verbose_name="详细地址")
    u_code=models.CharField(max_length=7,verbose_name="邮编")
    phone=models.CharField(max_length=14,verbose_name="手机号")
    login=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)
    address_status=models.IntegerField(choices=addr_status,default=2)