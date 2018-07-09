from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from article.models import Article
from api.resources import Resource
import json
from api.decorators import my_login_required
from comment.models import Comment
from api.common import Register
from user.models import User
# Create your views here.
class Mian(Resource):
    def get(self,request,*args,**kwargs):
        articles = Article.objects.filter()
        data = {}
        for article in articles:
            data['title']=article.title
            data['content']=article.content

        return JsonResponse(data,safe=False)

class Show(Resource):

    def get(self,request,pk,*args,**kwargs):

        articles = Article.objects.filter(pk=pk)
        data = {}
        for article in articles:
            data['title'] = article.title
            data['content'] = article.content

        return JsonResponse(data, safe=False)

    # @my_login_required
    def post(self, request, pk, *args, **kwargs):
        if 'username' not in request.session.keys():
            return HttpResponse('请先登录')
        else:
            data = json.loads(request.body.decode())
            articles = Article.objects.filter(pk=pk).first()
            user = request.session['username']
            users = User.objects.filter(username=user).first()
            text = data.get('text', '')
            comment = Comment()
            comment.article = articles
            comment.user = users
            comment.text = text
            comment.save()
            return HttpResponse('评论成功')

# class Comments(Resource):
#     def get(self,request,*args,**kwargs):
#         return render(request,'article.html')
