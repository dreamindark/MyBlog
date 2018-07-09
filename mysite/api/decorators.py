from django.shortcuts import redirect,render


def my_login_required(view_function):
    def wrap(request,*args,**kwargs):
        if 'username' not in request.session.keys():
            return render(request,'login.html')
        return view_function(request,*args,**kwargs)
    return wrap