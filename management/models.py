from django.db import models

# Create your models here.
class Address(models.Model):
    street_name = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateTimeField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

class Car(models.Model):
    MODEL_CHOICES = [
        ('model1', 'Model 1'),
        ('model2', 'Model 2'),
        ('model3', 'Model 3'),
    ]
    MANUFACTURER_CHOICES = [
        ('manufacturer1', 'Manufacturer 1'),
        ('manufacturer2', 'Manufacturer 2'),
        ('manufacturer3', 'Manufacturer 3'),
    ]
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    ]

    model_name = models.CharField(max_length=20, choices=MODEL_CHOICES)
    manufacturing_date = models.DateTimeField()
    manufacturer = models.CharField(max_length=20, choices=MANUFACTURER_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
