# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
#from django.contrib.auth.hashers import make_password


def index(request):
     return render(request, 'adminpanel/adminhome.html')

def create(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    password = str(hash(password))
    address = request.POST['address']
    pincode = request.POST['pincode']
    state = request.POST['state']
    city = request.POST['city']



    return HttpResponse(name+email+password+address+state+city)

