from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.

def index(request):
    return HttpResponse("<h1>welcome to views of myapp</h1>")

def home(request):
    return render(request,"myapp/home.html",{'name':"abhilash"})

def fact(request,n):
    n=int(n)
    return HttpResponse("<h1>factorial  of  value {} is:{}</h1>".format(n,factorial(n)))