from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="admin-index"),
<<<<<<< HEAD
    path("/register",views.register,name="admin-register"),
    path("/u",views.home,name="admin-home"),
=======
    path("api/bloodbanks", views.BloodBankView.as_view(), name="getbanks"),
    path("register/create", views.CreateView.as_view(), name="admin-create"),
>>>>>>> 396f66fc281a4b45a232c4a53c17cdee4a4a0f69
]