from django.shortcuts import render

# Create your views here.
def adminhome(request):
    return render(request,'adminpanel/adminhome.html' )
