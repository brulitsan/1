from django.contrib.auth.models import User
from django.db import models


class Showroom (models.Model):
    showroomName = models.CharField('имя', default='', max_length=25)
    location = models.CharField('местоположение', max_length=35)
    cars = models.ManyToManyField('Car', through='CarInformation')

    def __str__(self):
        return f'{self.showroomName} |{self.location}'

    class Meta:
        verbose_name = 'автосалон'
        verbose_name_plural = 'автосалон'


class Car (models.Model):
    carModel = models.CharField('имя', default='', max_length=30)
    car_brand = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.carModel

    class Meta:
        verbose_name = 'машины'
        verbose_name_plural = 'машины'


class CarInformation (models.Model):
    oil = (
        (1, 'бензин'),
        (2, 'дизель'),
        (3, 'газ')
    )
    showroom = models.ForeignKey(Showroom, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    engine_capacity = models.DecimalField(max_digits=30, decimal_places=2, default=0.0)
    fuelCriteria = models.SmallIntegerField(choices=oil, default=1)
    yearOfRelease = models.IntegerField(default=0)
    wheelLocation = models.CharField(max_length=30, default='')
    color = models.CharField(max_length=100, default='', )

    class Meta:
        verbose_name = 'информация о машинах'
        verbose_name_plural = 'информация о машинах'


class Buyer (models.Model):
    purchases = models.ManyToManyField(Car, related_name='покупки', verbose_name='покупки')
    buyerName = models.CharField(default='', max_length=30)
    price = models.IntegerField(default=0, verbose_name='цена')
    date = models.DateTimeField(default='')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.buyerName

    class Meta:
        verbose_name = 'покупатель'
        verbose_name_plural = 'покупатель'

