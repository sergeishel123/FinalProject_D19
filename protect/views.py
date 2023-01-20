from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.views.generic import TemplateView
from .models import OneTimeCode
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User

def protect_view(request):
    return render(request,'protect/protect.html',{})



def login_view(request):
    if request.user.is_authenticated:
        return redirect(to = 'personal')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email = email,password = password)
        if user is not None:
            code = random.choices('1234567890qwertyuiopasdfghjklzxcvbnm', k = 10)
            OneTimeCode.objects.create(user = user,code = ''.join(code))
            send_mail(
                subject = 'Код потверждения на сайте MMORPG',
                message = f'Здравствуйте, введите код потверждения   {"".join(code)}    для завершения аутентификации',
                from_email = 'sergeiazharkov@yandex.ru',
                recipient_list = [email]
            )
            return redirect('auth_code',user_id = user.id)
        error = True
        return HttpResponse(render(request,'protect/login.html',{'error': error}))
    if request.method == 'GET':
        return render(request,'protect/login.html',{})



def code_auth(request,user_id):
    if request.method == 'POST':
        code = request.POST['code']
        user = User.objects.get(id = user_id)
        if OneTimeCode.objects.filter(code = code).exists():
            login(request, user,backend = 'django.contrib.auth.backends.ModelBackend')
            return redirect(to = 'personal')
        else:
            error = True
            return render(request,'code.html',{'error': error})
    return render(request,'code.html',{})



