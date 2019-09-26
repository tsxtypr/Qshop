from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import hashlib
from django.core.paginator import Paginator
import random

# Create your views here.


# 设置加密
def setpassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    res=md5.hexdigest()
    return res

# 登录装饰器
def LoginValid(func):
    def inner(request,*args,**kwargs):
        email=request.COOKIES.get('email')
        session_email=request.session.get('email')
        if email and session_email:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Saller/login/')
    return inner


# 注册页面
def register(request):
    error=''
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
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
                    user.user_type=0
                    user.save()
                    return HttpResponseRedirect("/Saller/login/")
                else:
                    error='两次密码不一致'
        else:
            error='不能为空'

    return render(request,'saller/register.html',locals())

# 登录页面
def login(request):
    error=''
    if request.method=='POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if username and email and password:
            user=LoginUser.objects.filter(username=username,email=email,user_type=0).first()
            if user:
                check_pwd=LoginUser.objects.filter(password=setpassword(password)).first()
                if check_pwd:
                    response=HttpResponseRedirect("/Saller/index/")
                    response.set_cookie('email',email)
                    response.set_cookie('username',username)
                    response.set_cookie('userid',user.id)
                    request.session['email']=email
                    return response
                else:
                    error='密码不存在'
            else:
                error="该用户不存在"
        else:
            error="不能为空"
    return render(request,'saller/login.html',locals())

# 登出
def logout(request):
    response=HttpResponseRedirect('/Saller/login/')
    keys=request.COOKIES.keys()
    for each in keys:
        response.delete_cookie(each)
    request.session.flush()
    return response

# 首页
@LoginValid
def index(request):
    return render(request,'saller/index.html',locals())

# base页面
def base(request):
    return render(request,'saller/base.html')

# 商品页
def goods_list(request,type,page=1):
    page=int(page)
    if type == '0':
        goods=Goods.objects.filter(type=0).order_by('id')
    else:
        goods = Goods.objects.filter(type=1).order_by('id')
    paginator=Paginator(goods,10)
    page_obj=paginator.page(page)
    return render(request,'saller/goods_list.html',locals())


# 上架/下架的实现
def setstatus(request,status,id):
    id=int(id)
    good=Goods.objects.get(id=id)
    if status == 'up':
        good.type=1
    else:
        good.type = 0
    good.save()

    url=request.META.get('HTTP_REFERER','/Saller/goods_list/1/1/')
    return HttpResponseRedirect(url)

# 个人主页
def personal_info(request):
    email=request.COOKIES.get('email')
    user=LoginUser.objects.get(email=email)
    if request.method=='POST':
        data=request.POST
        user.username=data.get('username')
        user.email=data.get('email')
        user.phone_number=data.get('phone_number')
        user.age=data.get('age')
        user.gender=data.get('gender')
        user.address=data.get('address')
        if request.FILES.get('photo'):
            print(request.FILES.get('photo'))
            user.photo=request.FILES.get('photo')
        user.save()
    return render(request,'saller/personal_info.html',locals())


# 增加商品页
@LoginValid
def add_data(request):
    type=GoodsType.objects.all()
    if request.method=='POST':
        data=request.POST
        goods=Goods()
        goods.number=data.get('number')
        goods.name=data.get('name')
        goods.price=data.get('price')
        goods.count=data.get('count')
        goods.location=data.get('location')
        goods.safe_time=data.get('safe_time')
        goods.picture=request.FILES.get('picture')
        goods.save()
        goods_type=request.POST.get('goods_type')
        goods.goods_type=GoodsType.objects.get(id=goods_type)
        userid=request.COOKIES.get('userid')
        print(userid)
        goods.goods_store=LoginUser.objects.get(id=userid)
        goods.save()

    return render(request,'saller/add_data.html',locals())

