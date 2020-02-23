

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
    
    return render(request, 'adminpanel/adminhome.html')
