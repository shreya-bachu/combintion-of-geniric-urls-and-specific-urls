from django.shortcuts import render
from django.http import HttpResponse

def Hero(request):
    return HttpResponse("<h1> Alluarjun is hero of pushpa2</h1>")

def Heroine(request):
    return HttpResponse('<h1> Rashmika is heroine of pushpa2</h1>')

# Create your views here.
