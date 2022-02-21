from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        return render(request, 'signup.html')
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')