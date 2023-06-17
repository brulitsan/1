from django.contrib import admin
from .models import Showroom, Car, CarInformation, Buyer, Manager


@admin.register(Showroom)
class SalonAdmin(admin.ModelAdmin):
    list_display = ['showroomName', 'location']


@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['carModel', 'car_brand']


@admin.register(CarInformation)
class CarInformationAdmin(admin.ModelAdmin):
    list_display = ['car', 'showroom', 'price', 'quantity', 'engine_capacity',
                    'fuelCriteria', 'yearOfRelease', 'wheelLocation', 'color']

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['buyerName', 'price']
    filter_horizontal = ['products']

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass