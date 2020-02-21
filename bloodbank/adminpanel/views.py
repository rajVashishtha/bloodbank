from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def adminhome(request):
    return render(request,'adminpanel/adminhome.html' )

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        return HttpResponse(email)
