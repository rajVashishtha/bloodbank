from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="admin-index"),
    path("api/bloodbanks", views.BloodBankView.as_view(), name="getbanks"),
    path("register/create", views.CreateView.as_view(), name="admin-create"),
    path("login", views.login, name="admin-login"),
    path("home", views.home, name="admin-home"),
    path("logout", views.logout, name="admin-logout"),
    path("update", views.update, name="admin-update"),
    path("loginerror", views.login_error, name="admin-login-error")
]