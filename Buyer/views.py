from django.shortcuts import render
import hashlib
from Saller.models import *
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
import math
from django.core.paginator import Paginator
from Buyer.models import *
import time
from alipay import AliPay
from Qshop.settings import alipay_private_key_string,alipay_public_key_string
# Create your views here.

def setpassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    res=md5.hexdigest()
    return res

# 登录装饰器
def LoginValid(func):
    def inner(request,*args,**kwargs):
        id=request.COOKIES.get('id')
        session_id=request.session.get('id')
        if id and session_id:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Buyer/login/')
    return inner


# 注册页面
def register(request):
    error=''
    if request.method=='POST':
        username=request.POST.get('user_name')
        email=request.POST.get('email')
        password=request.POST.get('pwd')
        password2=request.POST.get('cpwd')
        print(username,email,password,password2)
        if username and email and password2 and password:
            user=LoginUser.objects.filter(email=email).first()
            if user:
                error = '该用户存在'
            else:
                if password2==password:
                    user=LoginUser()
                    user.username=username
                    user.password=setpassword(password)
                    user.email=email
                    user.save()
                    return HttpResponseRedirect("/Buyer/login/")
                else:
                    error='两次密码不一致'
        else:
            error='不能为空'

    return render(request,'buyer/register.html',locals())

# 登录页面
def login(request):
    error=''
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("pwd")
        if username and  password:
            user=LoginUser.objects.filter(username=username,user_type=1).first()
            if user:
                check_pwd=LoginUser.objects.filter(password=setpassword(password)).first()
                if check_pwd:
                    response=HttpResponseRedirect("/Buyer/index/")
                    response.set_cookie('username',username)
                    response.set_cookie('id',user.id)
                    request.session['id']=user.id
                    return response
                else:
                    error='密码不存在'
            else:
                error="该用户不存在"
        else:
            error="不能为空"
    return render(request,'buyer/login.html',locals())

# 首页
@LoginValid
def index(request):
    return render(request,'buyer/index.html',locals())

# 登出
def logout(request):
    response=HttpResponseRedirect('/Buyer/login/')
    keys=request.COOKIES.keys()
    for each in keys:
        response.delete_cookie(each)
    del request.session['id']
    return response

def user_center_info(request):
    return render(request,'buyer/user_center_info.html',locals())

def base(request):
    return render(request,'buyer/base.html')


# 起始页
def index(request):
    # 首先获取到类型
    result=[]
    goods_type=GoodsType.objects.all()
    for ty in goods_type:
        if len(ty.goods_set.order_by('-price'))>=4:
            result.append({
                'type':ty,
                'data':ty.goods_set.order_by('-price')[:4]
            })
    return render(request,'buyer/index.html',locals())

# 商品列表类
@LoginValid
def goods_list(request,page=1):
    page=int(page)
    type_id=request.GET.get('keyword')
    req_type=request.GET.get('req_type')
    if req_type=='findall':
        # 分页
        type = GoodsType.objects.get(id=type_id)
        goods = type.goods_set.all()
    elif req_type=='search':
        goods=Goods.objects.filter(name__contains=type_id)
    paginator = Paginator(goods, 15)
    page_obj = paginator.page(page)

    # 使推荐和展示的主页面和谐
    nums=math.ceil(len(goods.order_by('-price'))/5)
    recommend=goods.order_by('-price')[:nums]

    return render(request,'buyer/goods_list.html',locals())

# 商品详情页
@LoginValid
def detail_info(request):
    goods_id=request.GET.get('goodsid')
    goods=Goods.objects.get(id=goods_id)

    # 推荐同类型的两个商品
    type_id=goods.goods_type
    recommend=Goods.objects.filter(goods_type=type_id)[:2]
    return render(request,'buyer/detail_info.html',locals())

# 订单页面
@LoginValid
def pay(request):
    # 获取good_id商品id  goods_count商品数量
    good_id=request.GET.get("good_id")
    goods_count=request.GET.get("goods_count")
    if good_id and goods_count:
        good_id=int(good_id)
        print(good_id)
        goods_count=int(goods_count)
        print(goods_count)
        # 保存订单

        #     订单表
        payorder=PayOrder()
        ordernumber=str(time.time()).replace('.',"")
        payorder.order_number=ordernumber
        payorder.order_status=0
        # 获得商品价格
        price=Goods.objects.get(id=good_id)
        payorder.order_total=price.price*goods_count
        print(price.price*goods_count)
        # 获得用户id
        userid=request.COOKIES.get('id')
        payorder.order_user=LoginUser.objects.get(id=userid)
        payorder.save()

        # 订单详情表
        orderinfo=OrderInfo()
        orderinfo.order_id=payorder
        orderinfo.good_id=Goods.objects.get(id=good_id)
        orderinfo.goods_count=goods_count
        orderinfo.goods_tatol_price=payorder.order_total
        orderinfo.store_id=LoginUser.objects.get(id=userid)
        orderinfo.goods_price=Goods.objects.get(id=good_id).price
        orderinfo.save()

    return render(request,'buyer/pay.html',locals())


# 进行交易
@LoginValid
def AlipayViews(request):
    # 实例化支付对象
    alipay = AliPay(
        appid='2016101300673931',
        app_notify_url=None,
        app_private_key_string=alipay_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
    )

    order_id=request.GET.get("order_id")
    payorder=PayOrder.objects.get(id=order_id)
    # 实例化订单
    order_string = alipay.api_alipay_trade_page_pay(
        # 交易主体
        subject='天天生鲜',
        out_trade_no=payorder.id,
        total_amount=str(payorder.order_total),
        # 请求支付，之后及时回调的一个接口
        return_url="http://127.0.0.1:8000/Buyer/payresult/",
        # 通知地址
        notify_url="http://127.0.0.1:8000/Buyer/payresult/",
    )

    # 发送支付请求

    # 请求地址    支付网关+实例化订单
    result = "https://openapi.alipaydev.com/gateway.do?" + order_string
    print(result)

    return HttpResponseRedirect(result)


# 返回交易结果
def payresult(request):
    out_trade_no=request.GET.get("out_trade_no")
    payorder=PayOrder.objects.get(id=out_trade_no)
    payorder.order_status=1
    payorder.save()
    return render(request,'buyer/payresult.html')