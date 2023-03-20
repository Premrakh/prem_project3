from django.urls import path 
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('add_member/', add_member, name='add_member'),
    path('register/',register , name='register'),
    path('otp/',otp , name='otp'),
    path('login/',login , name='login'),
    path('logout/',logout , name='logout'),
    path('member_otp/',member_otp , name='member_otp'),
    path('watchman_otp/',watchman_otp , name='watchman_otp'),
    path('add_watchman/',add_watchman , name='add_watchman'),
    path('index2/',index2 , name='index2'),
    path('event/', event , name='event'),
    path('notice/', notice , name='notice'),
    path('add_notice/', add_notice , name='add_notice'),
    
]
