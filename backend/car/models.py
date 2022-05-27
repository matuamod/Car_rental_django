from django.db import models
from django.urls import reverse
from car_type.models import Car_Type

class Car(models.Model):
    car_id = models.AutoField
    car_brand = models.CharField(
        max_length=50, verbose_name='Car brand', null=False
    )
    car_model = models.CharField(
        max_length=50, verbose_name='Car model'
    )
    car_type = models.ForeignKey(
        Car_Type, on_delete=models.CASCADE
    )
    car_fuel_type = models.CharField(
         max_length=50, verbose_name='fuel type', null=False
    )
    count_of_seats = models.IntegerField()
    car_color = models.CharField(
        max_length=50, verbose_name='Car color'
    )
    car_plate = models.CharField(
        max_length=15, verbose_name='Car plates', null=False
    )
    car_image1 = models.ImageField(upload_to='images/car_images/')
    car_image2 = models.ImageField(upload_to='images/car_images/')
    car_image3 = models.ImageField(upload_to='images/car_images/')
    car_description = models.CharField(max_length=100)
    price_per_day = models.IntegerField()
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name='URL'
    )

    def __str__(self):
        return f'{self.car_brand} {self.car_model}: {self.car_plate}'

    def get_absolute_url(self):
        return reverse('ShowCar', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['car_brand', 'car_model', 'car_plate']

