from django.shortcuts import render,redirect
from accounts.form.login import LoginFrom
from .backends import EmailBackend
from django.contrib.auth import login as signin
from .models import Admin
# Create your views here.
def login(request):
    
    # print(request.session['user_id'])
    
    print(request.session.has_key('user_id'))
    form = LoginFrom()
    return render(request, 'auth/login.html',{'form':form,'error':request.session.get('error')})

def handle_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        admin = Admin.objects.get(email=email,password=password)
        request.session['user_id']=admin.id_admin
        return redirect('/products')
    except:
        request.session["error"] = "Email atau Password Salah"
        return redirect('/auth/login')
    # user = EmailBackend.authenticate(email,password)
    # signin(request,user,backend='accounts.backends.EmailBackend')
    # request.session['user_id']=user.id
    # return render(request, 'auth/login.html')