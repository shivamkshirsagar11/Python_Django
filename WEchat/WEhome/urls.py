from django.contrib import admin
from django.urls import path
from WEhome import views as v
urlpatterns = [
    path('',v.login,name="login" ),
    path('signup',v.signup,name="signup" ),
    path('img',v.img,name="signup" ),
    path('home',v.home,name="homepage" ),
]