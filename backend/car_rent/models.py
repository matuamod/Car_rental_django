from django.db import models

class RentCar(models.Model):
    rent_car_id = models.AutoField
    rent_car_brand = models.CharField(
        max_length=50, verbose_name='Rent car brand', null=False 
    )
    rent_car_model = models.CharField(
        max_length=50, verbose_name='Rent car model', null=False
    )
    rent_car_plate = models.CharField(
        max_length=50, verbose_name='Rent car plates', null=False
    )
    date_of_booking = models.DateField(blank=True,null=True)
    date_of_return = models.DateField(blank=True,null=True)
    total_days = models.IntegerField()
    total_price = models.IntegerField()
    customer_email = models.CharField(
        max_length=50, verbose_name='Customer_email', null=False
    )
    rent_status = models.BooleanField()