from django.shortcuts import render
from django.http import HttpResponse

def SK(request):
    return HttpResponse('<h1> Siva kartikeyan is hero of Amaran</h1>')
def SP(request):
    return HttpResponse('<h1> Sai pallavi is heroine of Amaran</h1>')

# Create your views here.
