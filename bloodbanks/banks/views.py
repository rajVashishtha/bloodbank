from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import BloodBag

def index(request):
    context = {
       "bloodbags": BloodBag.objects.all()
    }
    return render(request, 'banks/index.html', context)