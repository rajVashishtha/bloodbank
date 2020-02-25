# Create your views here.
import hashlib
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
#from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.response import Response

from banks.serializers import BloodBankSerializer, DynamicSerializer
from banks.models import  BloodBank, BloodBag

def index(request):
     return render(request, 'adminpanel/adminhome.html')



class CreateView(APIView):
    def post(self, request, *args, **kwargs):
        password = request.data['password']
        serializer = BloodBankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = hashlib.sha512(password.encode()).hexdigest()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    


class BloodBankView(APIView):
    def get(self, request, *args, **kwargs):
        # return HttpResponse(request.query_params)
        blood_group = request.query_params['blood_group']
        total_ml = request.query_params['total_ml']
        blood_bags = BloodBag.objects.filter(blood_group=blood_group, total_ml__gte=total_ml) #all id's
        li = [i.id for i in blood_bags]
        blood_banks = BloodBank.objects.filter(id__in=li)
        serializer = DynamicSerializer(blood_banks, many=True)
        return Response(serializer.data)






