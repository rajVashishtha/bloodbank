from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def adminhome(request):
    return render(request,'adminpanel/adminhome.html' )

def register(request):
    if request.method == 'POST':
        name = request.POST['organisation']
        address = request.POST['organisation_address']
        email = request.POST['email']
        password = request.POST['password']

        users = User()
        users.name = name
        users.address = address
        users.email = email
        users.password = password
        users.save()

        return HttpResponse(address)
