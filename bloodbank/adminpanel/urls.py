from django.urls import path
from . import views
urlpatterns = [
    path('',views.adminhome,name='adminhome'),
    path('register',views.register,name='adminregister'),
]