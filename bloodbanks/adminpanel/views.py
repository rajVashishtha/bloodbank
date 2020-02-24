# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
#from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.response import Response

from banks.serializers import BloodBankSerializer
from banks.models import  BloodBank, BloodBag

def index(request):
     return render(request, 'adminpanel/adminhome.html')

<<<<<<< HEAD
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
=======


class CreateView(APIView):
    def post(self, request, *args, **kwargs):
        # li = request.data['password']
        # request.data['password'] = hash(li)
        # li.append(hash(password))
        print("Request data: ", request.data)
        return HttpResponse(request.data)
        serializer = BloodBankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    


class BloodBankView(APIView):
    def get(self, request, *args, **kwargs):
        # return HttpResponse(request.query_params)
        blood_group = request.query_params['blood_group']
        total_ml = request.query_params['total_ml']
        qs = BloodBag.objects.filter(blood_group=blood_group, total_ml__gte=total_ml) #all id's
        li = [i.id for i in qs]
        qs2 = BloodBank.objects.filter(id__in=li)
        serializer = BloodBankSerializer(qs2, many=True)
        return Response(serializer.data)






>>>>>>> 396f66fc281a4b45a232c4a53c17cdee4a4a0f69
