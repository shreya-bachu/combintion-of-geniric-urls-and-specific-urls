from django.shortcuts import render
from django.http import HttpResponse

def hero(request):
    return HttpResponse('<h1>Alluarjun is hero of pushpa1</h1>')

def heroine(request):
    return HttpResponse('<h1>Rashmika is heroine of pushpa1</h1>')

# Create your views here.
