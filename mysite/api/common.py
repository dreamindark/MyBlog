from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import gvcode
from django.contrib.auth.hashers import make_password,check_password
from user.models import User
from api.resources import Resource
import json

class Get_code(Resource):
    def get(self,request,*args,**kwargs):
        base64_code,str_code = gvcode.base64()
        request.session['verify_code'] = str_code
        return HttpResponse(base64_code)

class Login(Resource):
    # def get_code(self,request):
    #     base64_code,str_code = gvcode.base64()
    #     request.session['verify_code'] = str_code
    #     return HttpResponse(base64_code)
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

    def post(self,request,*args,**kwargs):
        error = {}
        # data = request.POST
        data = json.loads(request.body.decode())
        username = data.get('username','')
        password = data.get('password','')
        verify = data.get('verify','')
        str_code = request.session['verify_code']
        user = User.objects.filter(username=username).first()
        if not username:
            error['username'] = '用户名不能为空'
        elif not password:
            error['password'] = '密码不能为空'
        elif not check_password(password,user.password):
            error['password'] = '密码错误'
        elif verify.upper() != str_code.upper():
            error['verify'] = '验证码错误'
        if not error:

            request.session['username'] = username
            return HttpResponse('登录成功')
        else:
            return JsonResponse(error,safe=False)



class Logout(Resource):
    def get(self,request,*args,**kwargs):
        try:
            del request.session['username']
        except:
            pass
        return HttpResponse('您已经登出')


class Register(Resource):

    def get(self,request,*args,**kwargs):
        return render(request,'register.html')
    def post(self,request,*args,**kwargs):
        error = {}
        data = json.loads(request.body.decode())
        username = data.get('username','')
        password = data.get('password','')
        password2 = data.get('password2','')
        tel = data.get('tel','')
        user = User.objects.filter(username = username).first()
        if not username:
            error['username'] = '用户名不能为空'
        elif user is not None:
            error['username'] = '该用户名已被使用'
        elif not password:
            error['password'] = '密码不能为空'
        elif password !=password2:
            error['password2'] = '前后密码不一致'
        if not error:
            user = User()
            user.username = username
            user.password = make_password(password)
            user.tel = tel
            user.save()
            return HttpResponse('注册成功')
        else:
            return JsonResponse(error,safe=False)