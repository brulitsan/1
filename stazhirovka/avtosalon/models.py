from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver


class User(AbstractUser):
    def get_manager(self):
        try:
            return self.manager
        except:
            return None

class Showroom (models.Model):
    showroomName = models.CharField('название', default='', max_length=25)
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
    quantity = models.IntegerField(default=0)
    engine_capacity = models.DecimalField(max_digits=30, decimal_places=2, default=0.0)
    fuelCriteria = models.SmallIntegerField(choices=oil, default=1)
    yearOfRelease = models.IntegerField(default=0)
    wheelLocation = models.CharField(max_length=30, default='')
    color = models.CharField(max_length=100, default='', )

    def __str__(self):
        return f'{self.car.carModel}'

    class Meta:
        verbose_name = 'информация о машинах'
        verbose_name_plural = 'информация о машинах'


class Buyer (models.Model):
    products = models.ManyToManyField(CarInformation, related_name='покупки', verbose_name='покупки')
    buyerName = models.CharField(default='', max_length=30)
    price = models.IntegerField(default=0, verbose_name='цена')
    date = models.DateTimeField(default='')
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.buyerName

    class Meta:
        verbose_name = 'покупатель'
        verbose_name_plural = 'покупатель'


@receiver(m2m_changed, sender=Buyer.products.through)
def update_product_quantity(sender, instance, **kwargs):
    if kwargs.get('action') == 'post_add':
        # при добавлении новых товаров
        # уменьшаем количество товара на количество заказанных единиц
        for product in instance.products.all():
            product.quantity -= instance.quantity
            product.save()

class Manager (models.Model):
    # Clients = models.ForeignKey(Buyer, related_name='клиент', verbose_name='клиент', on_delete=models.PROTECT, null=True)
    ManegerName = models.CharField(default='', max_length=30)
    user = models.OneToOneField(User, verbose_name='Менеджер', on_delete=models.CASCADE)

    def __str__(self):
        return self.ManegerName

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджер'
