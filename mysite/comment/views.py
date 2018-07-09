# from django.shortcuts import render
# import json
# from django.http import HttpResponse
# from comment.models import Comment
# from api.resources import Resource
# # Create your views here.
#
#
#
# class Comments(Resource):
#     def get(self,request,*args,**kwargs):
#         return render(request,'article.html')
#     def post(self,request,*args,**kwargs):
#         data = json.loads(request.body.decode())
#         content = data.get('comment')
#         id = data.get('id')
#         name = data.get('name')
#         comment = Comment()
#         comment.text = content
#         comment.article = id
#         comment.user = name
#         comment.save()
#         return HttpResponse('评论成功')