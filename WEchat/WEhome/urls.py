from django.contrib import admin
from django.urls import path
from WEhome import views as v
urlpatterns = [
    path('',v.login,name="login" ),
    path('signup',v.signup,name="signup" ),
    path('home',v.home,name="homepage" ),
    path('change',v.change,name="change" ),
    path('logout',v.logout,name="logout" ),
]