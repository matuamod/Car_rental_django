from django.db import models

class Car_Type(models.Model):
    car_type_id = models.AutoField
    car_type = models.CharField(
        max_length=50, verbose_name='Car type', null=False
    )

    def __str__(self): 
        return f'{self.car_type}'

