from django.shortcuts import render,redirect,HttpResponse
from WEhome.models import BaseProfile as bp,FullProfile as fp
from django.contrib import messages
import bcrypt
from django.core.cache import cache
from django.http import HttpRequest
from django.utils.cache import get_cache_key
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        request.session["email"] = email
        ins_user = bp.objects.filter(email=email).first()
        ins_user_full = fp.objects.filter(bpu_id = ins_user.id).first()
        if ins_user:
            if bcrypt.checkpw(password.encode('utf-8'), ins_user.password.encode('utf-8')):
                return render(request, 'home.html',{"user":ins_user,"fullp":ins_user_full})
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
        fullp = fp(bpu = basep)
        fullp.save()
        messages.success(request,"Your account created successfully!")
        return redirect('/')
    return render(request, 'signup.html')

def change(request):
    email =  request.session["email"]
    ins_user = bp.objects.filter(email=email).first()
    ins_user_full = fp.objects.filter(bpu_id = ins_user.id).first()
    if ins_user:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            use = request.POST['use']
            address = request.POST['address']
            city = request.POST['city']
            pincode = request.POST['pin']
            image = request.FILES['userImg']

            ins_user.name = name
            ins_user.email = email
            ins_user.usePurpose = use
            ins_user.save()

            ins_user_full.profileImg = image
            ins_user_full.address = address
            ins_user_full.city = city
            ins_user_full.pincode = pincode
            ins_user_full.save()
            return render(request, 'home.html',{"user":ins_user,"fullp":ins_user_full})
        return render(request, 'changeprofile.html',{"user":ins_user,"fullp":ins_user_full})

def home(request):
    if request.method != 'POST':
        return render(request, 'login.html')
    else: return redirect('/')