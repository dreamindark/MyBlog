from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf.urls import url

class Api(object):

    def __init__(self,name = 'v1'):
        self.name = name
        self.resources = []

    def add_resource(self,resource):
        self.resources.append(resource)

    @property
    def urls(self):

        patterns = [ url(r'^{version}/{name}/(?P<pk>[0-9]+)?'.format(version = self.name,name=resource.name),
        resource.process_request)
            for resource in self.resources
        ]
        return patterns

class Resource(object):

    def __init__(self,name = None):
        self.name = name or self.__class__.__name__.lower()

    def process_request(self,request,*args,**kwargs):
        method = request.method
        if method == 'GET':
            return self.get(request,*args,**kwargs)
        elif method == 'POST':
            return self.post(request,*args,**kwargs)
        elif method == 'PUT':
            return self.put(request,*args,**kwargs)
        elif method == 'DELETE':
            return self.delete(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return HttpResponse('GET')

    def post(self,request,*args,**kwargs):
        return HttpResponse('POST')

    def put(self,request,*args,**kwargs):
        return HttpResponse('PUT')

    def delete(self,request,*args,**kwargs):
        return HttpResponse('DELETE')






