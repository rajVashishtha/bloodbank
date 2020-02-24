# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
     return render(request, 'adminpanel/adminhome.html')

def home(request):
     return render(request , "adminpanel/controlpanel.html")

def register(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    address = request.POST['address']
    pincode = request.POST['pincode']
    state = request.POST['state']
    city = request.POST['']
