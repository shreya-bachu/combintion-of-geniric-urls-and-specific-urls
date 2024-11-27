from django.shortcuts import render
from django.http import HttpResponse

def kiran(request):
    return HttpResponse('<h1> Kiran is hero of KA</h1>')
def heroine1(request):
    return HttpResponse('<h1> Anjali is heroine of KA')


# Create your views here.
