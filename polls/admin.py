from django.contrib import admin
from .models import Customer, Car, CarRent
# Register your models here.

admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(CarRent)