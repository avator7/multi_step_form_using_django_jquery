from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, request
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.utils import json
from django.http import HttpResponse, HttpRequest
from .models import *
from .forms import CustomerForm, AddressForm, CarForm
# Create your views here.

@api_view(['GET'])
def getadminhealth(requests):
    return Response("ok")


def multi_step_form(request):
    customer_form = CustomerForm()
    address_form = AddressForm()
    car_form = CarForm()
    return render(request, 'multi_step_form.html', {'customer_form': customer_form, 'address_form': address_form, 'car_form': car_form})

@api_view(['POST'])
def save_form(request):
    data = request.data
    fname = str(data['first_name'])
    lname = str(data['last_name'])
    age = int(data['age'])
    dob = str(data['date_of_birth'])
    phone = str(data['phone'])
    email = str(data['email'])
    street_name = str(data['street_name'])
    pincode = str(data['pincode'])
    city = str(data['city'])
    state = str(data['state'])
    country_code =  str(data['country_code'])
    model_name =  str(data['model_name'])
    manufacturing_date = str(data['manufacturing_date'])
    manufacturer = str(data['manufacturer'])
    color = str(data['color'])

    address = Address(street_name=street_name, pincode=pincode, city=city, state=state, country_code=country_code)
    address.save()
    customer =  Customer(first_name=fname, last_name=lname, age=age, date_of_birth=dob, email=email, phone=phone, address=address)
    customer.save()
    car = Car(model_name=model_name, manufacturing_date=manufacturing_date, manufacturer=manufacturer, color=color, customer=customer)
    
    return Response("data stored successfully", status=200)
