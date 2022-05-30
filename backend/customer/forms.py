import time
from urllib import request
from django import forms
from django.shortcuts import redirect, render
from .forms import *
from .models import Customer


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_fname', 'customer_lname',
                  'customer_db', 'customer_gender',
                  'customer_address', 'customer_email',
                  'customer_password', 'customer_number',
                  'customer_city', 'customer_license']


class CustomerLoginForm(forms.Form):
    customer_email = forms.CharField(max_length=40)
    customer_password = forms.CharField(max_length=30)


class ChooseCarForm(forms.Form):
    car_type = forms.CharField(max_length=50)
    car_brand = forms.CharField(max_length=50)
    car_fuel_type = forms.CharField(max_length=50)
    price_per_day = forms.CharField(max_length=50)


class CheckAvailabilityForm(forms.Form):
    date_of_booking = forms.DateField(required=True, input_formats=["%Y-%m", ])
    date_of_return = forms.DateField(required=True, input_formats=["%Y-%m", ])
    print(date_of_booking)
    print(date_of_return)
    print('Hi matua')
