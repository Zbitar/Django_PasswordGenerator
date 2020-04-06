from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,"generator/home.html",{"password":"sssss"})


def about(request):
    return render(request,"generator/about.html")


def password(request):
    password=""
    letters="abcdefghijklmnopqrstuvwxyz"
    lowcharacters=list(letters)
    uppcharacters=list(letters.upper())
    special=list("?/.,;(&%$@!)")
    length=int(request.GET.get("length",6))
    if(request.GET.get("UpperCase")):
        lowcharacters.extend(uppcharacters)
    
    if(request.GET.get("SpecialChar")):
        lowcharacters.extend(special)
    
    for i in range(length):
        password+=random.choice(lowcharacters)

    return render(request,"generator/password.html",{"password":password})
