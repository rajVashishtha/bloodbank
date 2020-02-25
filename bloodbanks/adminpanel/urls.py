from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="admin-index"),
    path("home/",views.home,name="admin-home"),
    path("api/bloodbanks", views.BloodBankView.as_view(), name="getbanks"),
    path("register/create", views.CreateView.as_view(), name="admin-create"),
]