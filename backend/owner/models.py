from django.db import models


class Owner(models.Model):
    owner_id = models.AutoField
    owner_fname = models.CharField(
        max_length=30, verbose_name='First name', null=False
    )
    owner_lname = models.CharField(
        max_length=30, verbose_name='Last name', null=False
    )
    owner_db = models.DateField()

    man = 'man'
    woman = 'woman'

    gender_type = (
        (man, 'man'),
        (woman, 'woman'),
    )

    owner_gender = models.CharField(
        max_length=10, verbose_name='gender', choices=gender_type
    )
    owner_address = models.CharField(
        max_length=50, verbose_name='Address'
    )
    owner_email = models.CharField(
        max_length=40, verbose_name='email', null=False, unique=True
    )
    owner_password = models.CharField(
        max_length=30, verbose_name='email password', null=False, unique=True
    )
    owner_number = models.CharField(
        max_length=20, verbose_name='Telephone_number', null=False, unique=True
    )
    owner_city = models.CharField(
        max_length=20, verbose_name='City'
    )
    owner_drive_license = models.ImageField(upload_to='images/Owner_License/')
    isOwner = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.owner_email}: {str(self.owner_drive_license)}'