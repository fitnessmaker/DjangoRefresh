from django.shortcuts import render
from django.http import HttpResponse

from .models import Members,Appartment
# Create your views here.




#def team(request):

#    mems = Members.objects.all()

#    return render(request,"index.html",{"members": mems})


def villas(request):
    
    vill = Appartment.objects.all()

    return render(request,"index.html",{"homes": vill})


def about(request):

    return render(request,"about.html")