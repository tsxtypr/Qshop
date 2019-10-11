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
# import logging
# collect=logging.getLogger("django")
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
                    # collect.info("--------%s is login-----------"% user.username)
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

# 个人中心页
@LoginValid
def user_center_info(request):
    return render(request,'buyer/user_center_info.html',locals())

def base(request):
    return render(request,'buyer/base.html')

# from django.views.decorators.cache import cache_page
# @cache_page(60*20)  #视图当中使用缓存，缓存寿命20分钟
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
        print(goods)
        paginator = Paginator(goods, 15)
        page_obj = paginator.page(page)
    elif req_type=='search':
        goods=Goods.objects.filter(name__contains=type_id)
        paginator = Paginator(goods, 15)
        page_obj = paginator.page(page)

    # 使推荐和展示的主页面和谐
    if len(goods)>=1:
        nums=math.ceil(len(page_obj)/5)
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

# 单个订单
# 立即购买页面
@LoginValid
def pay(request):
    # 获取good_id商品id  goods_count商品数量
    goods_id=request.GET.get("good_id")
    goods_count=request.GET.get("goods_count")
    if goods_id and goods_count:
        good_id=int(goods_id)
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
        price=Goods.objects.get(id=goods_id)
        payorder.order_total=price.price*goods_count
        print(price.price*goods_count)
        # 获得用户id
        userid=request.COOKIES.get('id')
        payorder.order_user=LoginUser.objects.get(id=userid)
        payorder.save()

        # 订单详情表
        orderinfo=OrderInfo()
        orderinfo.order_id=payorder
        orderinfo.good_id=Goods.objects.get(id=goods_id)
        orderinfo.goods_count=goods_count
        orderinfo.goods_tatol_price=payorder.order_total
        orderinfo.store_id=LoginUser.objects.get(id=userid)
        orderinfo.goods_price=Goods.objects.get(id=goods_id).price
        orderinfo.save()

    addre_obj = RecAddress.objects.get(address_status=1)
    return render(request,'buyer/pay.html',locals())

# 多个订单
# 加入购物车的页面
@LoginValid
def paymore(request):
    data=request.GET
    # print(data)
    goods_info=[]
    total_price =0
    for key,val in data.items():
        if key.startswith("id"):
            goods_id=key.split("_")[1]
            cart_id=key.split("_")[-1]
            goods_count=sum(list(map(int,data.getlist("count_"+goods_id))))
            goods_info.append((int(goods_id),goods_count,int(cart_id)))
    print(goods_info)

    # 订单表
    payorder = PayOrder()
    ordernumber = str(time.time()).replace('.', "")
    # 给加入订单的商品加上一个统一的商品编号
    for each in goods_info:
        goods_id=each[-1]
        print(goods_id)
        each_cart=Cart.objects.get(id=goods_id)
        print(each_cart)
        each_cart.number=ordernumber
        each_cart.save()
    payorder.order_number = ordernumber
    payorder.order_status = 0
    # 因为商品价钱不能为空，所以先给一个默认值
    payorder.order_total = 0
    # 获得用户id
    userid = request.COOKIES.get('id')
    payorder.order_user = LoginUser.objects.get(id=userid)
    payorder.save()

    for each in goods_info:
        goods_id=each[0]
        goods_count=each[1]
        # print(goods_id,goods_count)

        # 订单详情表
        orderinfo=OrderInfo()
        orderinfo.order_id=payorder
        orderinfo.good_id=Goods.objects.get(id=goods_id)
        orderinfo.goods_count=goods_count
        orderinfo.goods_tatol_price=orderinfo.good_id.price*goods_count
        orderinfo.store_id=LoginUser.objects.get(id=userid)
        orderinfo.goods_price=Goods.objects.get(id=goods_id).price
        orderinfo.save()

        # 累加总价格
        total_price+=orderinfo.goods_tatol_price

    payorder.order_total = total_price
    payorder.save()
    # print(total_price)

    addre_obj=RecAddress.objects.get(address_status=1)
    return render(request,"buyer/pay.html",locals())

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
        out_trade_no=payorder.order_number,
        total_amount=str(payorder.order_total),
        # 请求支付，之后及时回调的一个接口
        return_url="http://127.0.0.1:8000/Buyer/payresult/",
        # 通知地址
        notify_url="http://127.0.0.1:8000/Buyer/payresult/",
    )

    # 发送支付请求

    # 请求地址    支付网关+实例化订单
    result = "https://openapi.alipaydev.com/gateway.do?" + order_string
    # print(result)

    return HttpResponseRedirect(result)


# 返回交易结果
def payresult(request):
    # 获得订单编号
    out_trade_no=request.GET.get("out_trade_no")
    print(request.GET)
    # 获得是哪笔订单
    payorder=PayOrder.objects.get(order_number=out_trade_no)
    payorder.order_status=1
    #从cart表中查询次笔订单的商品，并将他们的状态都改为1
    carts=Cart.objects.filter(number=out_trade_no)
    print(carts)
    # print(carts)
    # 将所有已经交易过的商品的状态都改为1
    for each_cart in carts:
        each_cart.status=1
        each_cart.save()
    payorder.save()
    return render(request,'buyer/payresult.html')


# 点击购物车图标，加入到购物车
def add_cart(request):
    result={
        'code':10000,
        'data':""
    }
    if request.method=="POST":
        goods_id=request.POST.get("goods_id")
        goods_number=float(request.POST.get("goods_number",1))
        user_id=request.COOKIES.get("id")
        # print(goods_id,goods_number)
        # print(user_id)

        goods=Goods.objects.get(id=goods_id)
        # print(goods)
        cart=Cart()
        # print('-----')
        cart.goods_number=goods_number
        cart.goods_price=goods.price
        cart.goods_total=goods.price*goods_number
        cart.goods=goods
        cart.cart_user=LoginUser.objects.get(id=user_id)
        cart.save()
        print(cart)
        print('----------')
        # print(cart)
        result["code"]=10000
        result["data"]="加入购物车成功"
    else:
        result["code"]=10001
        result["data"]="数据请求方式不正确"

    return JsonResponse(result)


# 购物车页面
@LoginValid
def cart(request):
    user_id=request.COOKIES.get("id")
    # 购物车对象  是个查询集
    cart=Cart.objects.filter(cart_user_id=user_id,status=0).order_by("-id")
    # 商品的总条数
    goods_number=cart.count()
    # print(cart)
    # print(goods_number)

    return render(request,'buyer/cart.html',locals())

#全部订单
@LoginValid
def allorder(request):
    userid=request.COOKIES.get('id')
    # print(userid)
    user=LoginUser.objects.get(id=userid)
    # print(user)
    all_payorder=user.payorder_set.order_by("-order_date")
    return render(request,'buyer/allorder.html',locals())

from CeleryTask.tasks import *
def reqtest(request):
    # 执行celery测试
    # test.delay()

    # 带参数的函数
    # name=request.GET.get('name')
    # age=request.GET.get('age')
    # print(name,age)
    # myprint.delay(name,age)


    # 短信
    message.delay()
    return HttpResponse('test')

from django.core.cache import cache
def cache_test(request):
    # 从缓存中提取数据
    # 根据订单编号，获取订单总价
    order_number=request.GET.get('order_number')
    data=cache.get(order_number)
    print('------------')
# 如果没有数据，数据查询，增加到缓存中
    if not data:
        print("+++++++++++")
        payorder=PayOrder.objects.filter(order_number=order_number).first()
        # 将数据写到cache
        cache.set(order_number,payorder.order_total,60)
        data=cache.get(order_number)
    return HttpResponse('order_number:%s'%data)

def rec_address(request):
    if request.method=="POST":
        data=request.POST
        # print(data)
        user_id=request.COOKIES.get("id")

        address=RecAddress()
        address.username=data.get("username")
        address.detail_addr=data.get("detail_addr")
        address.u_code=data.get("u_code")
        address.phone=data.get("phone")
        address.login=LoginUser.objects.get(id=user_id)
        address.save()

    #循环当前地址
    addresses=RecAddress.objects.all()

    # 获得当前地址的id
    address_data = request.GET
    if address_data:
        address_id = int(address_data.get("address_id"))
    else:
        address_id = RecAddress.objects.get(address_status=1).id
    print(address_id)
    # 将地址的状态改变
    addre_obj=RecAddress.objects.get(id=address_id)
    addre_obj.address_status=1
    RecAddress.objects.exclude(id=address_id).update(address_status=2)
    addre_obj.save()
    return render(request,'buyer/rec_address.html',locals())