from django.shortcuts import render
from accounts.form.login import LoginFrom
# Create your views here.
def login(request):
    form = LoginFrom()
    return render(request, 'auth/login.html',{'form':form})