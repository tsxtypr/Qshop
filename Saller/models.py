from django.db import models
from django.db.models import Manager

# Create your models here.
class LoginUser(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=32)
    username=models.CharField(max_length=32,null=True,blank=True)
#     null数据库中的数据可以为空，blank针对表单，表单中的数据可以不填
    phone_number=models.CharField(max_length=11,null=True,blank=True)
    photo=models.ImageField(upload_to='images',null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(null=True,blank=True,max_length=4)
    address=models.TextField(null=True,blank=True)
    # 1买家  0卖家  3管理员
    user_type=models.IntegerField(default=1)

    class Meta:
        db_table='loginuser'

# class MyGoodsType(Manager):
#     def myaddtype(self,type_label,type_description,picture='images/1.jpg'):
#         goodstype=GoodsType()
#         goodstype.type_label = type_label
#         goodstype.type_description = type_description
#         goodstype.picture = picture
#         goodstype.save()
#
#         return goodstype

class GoodsType(models.Model):
    type_label=models.CharField(max_length=32)
    type_description=models.TextField()
    picture=models.ImageField(upload_to='images')

    # objects=MyGoodsType()

TYPE_LIST=(
    (1,'上架'),
    (0,"下架"),
)
class Goods(models.Model):
    number=models.CharField(max_length=11)
    name=models.CharField(max_length=32)
    price=models.FloatField()
    count=models.IntegerField()
    location=models.CharField(max_length=254)
    safe_time=models.IntegerField()
    type=models.IntegerField(choices=TYPE_LIST,default=1)
    pro_time=models.DateField(auto_now=True,verbose_name='生产日期')
    goods_description=models.TextField(default='水果')
    goods_detaile=models.TextField(default="水果")
    picture=models.ImageField(upload_to="images")

    # 类型  一对多
    goods_type=models.ForeignKey(to=GoodsType,on_delete=models.CASCADE,default=1)
    # 店铺
    goods_store=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,default=1)
    class Meta:
        db_table='goods'

class Valid_Code(models.Model):
    code_content=models.CharField(max_length=8,verbose_name="验证码")
    code_time=models.DateTimeField(auto_now=True,verbose_name='创建时间')
    code_status=models.IntegerField(verbose_name="状态")  #1使用 0未使用
    code_user=models.EmailField(verbose_name="邮箱")
