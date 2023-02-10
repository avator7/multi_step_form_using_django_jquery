# forms.py
from django import forms
from .models import Customer, Address, Car

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'age', 'date_of_birth', 'phone', 'email']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_name', 'pincode', 'city', 'state', 'country_code']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model_name', 'manufacturing_date', 'manufacturer', 'color']
