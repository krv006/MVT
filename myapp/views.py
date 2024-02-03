from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    context = {
        
    }
    return render ( request ,context , 'index.html')




