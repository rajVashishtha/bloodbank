# Create your views here.
import hashlib
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
#from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.response import Response

from banks.serializers import BloodBankSerializer, DynamicSerializer
from banks.models import  BloodBank, BloodBag, Size, BloodGroup, TotalBlood

from .logic import init_bloodbags

def index(request):
    return render(request, 'adminpanel/adminhome.html')

def login_error(request):
    context = {
       "message": "Please Login First"
    }
    return render(request, 'adminpanel/adminhome.html', context)
   

def home(request):
    if not 'admin_id' in request.session:
        return HttpResponseRedirect(reverse("admin-login-error"))
        
    bank_id = request.session['admin_id']
    bank = BloodBank.objects.get(id=bank_id)
    
    sizes = Size.objects.all()
    groups = BloodGroup.objects.all()
    bloodbags = []

    for group in groups:
        query_set = BloodBag.objects.filter(blood_bank=bank, blood_group=group)
        bags_group = list(query_set)
        bloodbags.append(bags_group)

    context = {
        "bloodbags": bloodbags,
        "groups": groups
    }
    return render(request,'adminpanel/controlpanel.html', context)



def login(request):
    email = request.POST['email']
    password = request.POST['password']
    password = hashlib.sha512(password.encode()).hexdigest()

    try:
        bank = BloodBank.objects.get(email=email,password=password)
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse('admin-index'))

    q_email = bank.email 
    q_password = bank.password 
    q_id =  bank.id 
    q_name = bank.name
   

    if email == q_email and password == q_password:
        request.session['admin_id'] = q_id
        request.session['admin_name'] = q_name
        return HttpResponseRedirect(reverse('admin-home'))
    
    else:
        return HttpResponseRedirect(reverse('admin-index'))
   # return HttpResponse(query)


def logout(request):
    request.session.flush()
    print("hello")
    return HttpResponseRedirect(reverse('admin-index'))


def update(request):
    bank_id = request.session['admin_id']
    bank = BloodBank.objects.get(id=bank_id)
    bags = list(BloodBag.objects.filter(blood_bank=bank))
    groups = BloodGroup.objects.all()
    total, i, j = 0, 0, 0
    groups_total = []

    for bag in bags:
        if i != 0 and i % 5 == 0:
            groups_total.append(total)
            total = 0
        value = request.POST.get(str(bag.id), 0)
        blood_bag = BloodBag.objects.get(id=bag.id)
        blood_bag.quantity = value
        blood_bag.save()
        bag_size = blood_bag.size_in_ml
        total += int(value) * bag_size.size_in_ml
        i += 1

    groups_total.append(total)    
    for group in groups:
        total_obj = TotalBlood.objects.get(blood_bank=bank, blood_group=group)
        total_obj.total_ml = groups_total[j]
        total_obj.save()
        j += 1

    # new_update(request.session, values)   
    return HttpResponseRedirect(reverse('admin-home'))     


# class HomeView(APIView):
#     def get(self, request, *args, )




class CreateView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        if BloodBank.objects.filter(email=email).exists():
            return HttpResponseRedirect(reverse("admin-index"))
        password = request.data['password']
        serializer = BloodBankSerializer(data=request.data)

        if serializer.is_valid():
            hash_password = hashlib.sha512(password.encode()).hexdigest()
            serializer.validated_data['password'] = hash_password
            serializer.save()

            email = request.data['email']
            password = hash_password
            bank = BloodBank.objects.get(email=email,password=password)
            request.session['admin_id'] = bank.id
            request.session['admin_name'] = bank.name
            init_bloodbags(bank)
            return HttpResponseRedirect(reverse('admin-home'))

        return Response(serializer.errors)


class BloodBankView(APIView):
    def get(self, request, *args, **kwargs):
        # return HttpResponse(request.query_params)
        blood_group = request.query_params['blood_group']
        total_ml = request.query_params['total_ml']
        total_blood_objects = TotalBlood.objects.filter(blood_group=blood_group, total_ml__gte=total_ml) #all id's
        li = [i.blood_bank.id for i in total_blood_objects]
        blood_banks = BloodBank.objects.filter(id__in=li)
        serializer = DynamicSerializer(blood_banks, many=True)
        return Response(serializer.data)






