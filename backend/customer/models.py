from django.db import models
from django.forms import CharField


class Customer(models.Model):
    customer_id = models.AutoField
    customer_fname = models.CharField(
        max_length=30, verbose_name='First name', null=False
    )
    customer_lname = models.CharField(
        max_length=30, verbose_name='Last name', null=False
    )
    customer_db = models.DateField()

    man = 'man'
    woman = 'woman'

    gender_type = (
        (man, 'man'),
        (woman, 'woman'),
    )

    customer_gender = models.CharField(
        max_length=10, verbose_name='gender', choices=gender_type
    )
    customer_address = models.CharField(
        max_length=50, verbose_name='Address'
    )
    customer_email=models.CharField(
        max_length=40, verbose_name='email', null=False, unique=True
    )
    customer_password = models.CharField(
        max_length=30, verbose_name='email password', null=False, unique=True
    )
    customer_number = models.CharField(
        max_length=20, verbose_name='Telephone_number', null=False, unique=True
    )
    customer_city = models.CharField(
        max_length=20, verbose_name='City'
    )
    customer_drive_license = models.ImageField(upload_to='images/Customer_License/')

    def __str__(self):
        return f'{self.customer_email}: {str(self.customer_drive_license)})'