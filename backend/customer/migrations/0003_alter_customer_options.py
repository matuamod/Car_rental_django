# Generated by Django 4.0.4 on 2022-05-26 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_customer_license_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['customer_fname', 'customer_lname', 'customer_email']},
        ),
    ]
