from django.shortcuts import render
from django.http import HttpResponse
from .models import City
# Create your views here.

def index(request):
    return HttpResponse("hello railways")
def add_city(request):
    return render(request,'admin/add_city.html')
def insert_city(request):
    c=request.POST['city']
    a=City(city=c)
    a.save()
    return  HttpResponse(c+' inserted')