from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="admin-index"),
    path("/register",views.register,name="admin-register"),
    path("/u",views.home,name="admin-home"),
]