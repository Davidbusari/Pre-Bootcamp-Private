from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.reg_User),
    path('login', views.processlogin),
    path('congrats', views.display_congrats),
    path('logout', views.logout)

]