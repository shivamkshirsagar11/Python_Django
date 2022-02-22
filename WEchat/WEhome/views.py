from django.shortcuts import render,redirect,HttpResponse
from WEhome.models import BaseProfile as bp
from django.contrib import messages
import bcrypt
from django.core.cache import cache
from django.http import HttpRequest
from django.utils.cache import get_cache_key
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        ins_user = bp.objects.filter(email=email).first()
        if ins_user:
            if bcrypt.checkpw(password.encode('utf-8'), ins_user.password.encode('utf-8')):
                return render(request, 'home.html',{"name":ins_user})
            else:
                return HttpResponse("Password is wrong!!!!!")
        else:
            return HttpResponse("No user found!!!")
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        use = request.POST['type']
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14))
        basep = bp(name=name,email=email,usePurpose=use,password=hashed_pw.decode('utf-8'))
        basep.save()
        messages.success(request,"Your account created successfully!")
        return redirect('/')
    return render(request, 'signup.html')

def img(request):
    if request.method == 'POST':
        pass
    return render(request, 'test.html')

def home(request):
    if request.method != 'POST':
        return render(request, 'login.html')
    else: return redirect('/')