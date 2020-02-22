from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

# path("<int:bank_id>", views.bank, name="bank"),
# path("<int:bank_id>/update", views.update, name="update"),
