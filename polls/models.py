from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    driverlicense_num = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name
    
class Car(models.Model):
    model = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    features = models.CharField(max_length=50)
    availability = models.CharField(max_length=25)
    location = models.CharField(max_length=50)
    daily_rate = models.DecimalField(decimal_places=2, max_digits=10)
    CarRent = models.ManyToManyField(Customer, through='CarRent')

    def __str__(self):
        return self.model
    
    

class CarRent(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    rent_duration = models.IntegerField()
    payment = models.IntegerField()

    def __str__(self):
        return self.payment
    
    

# Create your models here.
