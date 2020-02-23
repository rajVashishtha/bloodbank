from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="admin-index"),
    path("/create",views.create,name="admin-create"),
]