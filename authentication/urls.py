from django.contrib import admin
from django.urls import path, include
from . import views
from .views import google_login, google_callback

urlpatterns = [
    path("",views.home,name="home"),
    path('landing',views.landing,name="landing"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    path("accounts/google/login/", google_login, name="google_login"),
    path("accounts/google/login/callback/", google_callback, name="google_callback"),
]