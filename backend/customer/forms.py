from django import forms
from .forms import *
from .models import Customer
from django.contrib.auth.forms import UserCreationForm


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_fname', 'customer_lname',
                  'customer_db', 'customer_gender',
                  'customer_address', 'customer_email',
                  'customer_password', 'customer_number',
                  'customer_city', 'customer_license']
        print(model.customer_fname)


class CustomerLoginForm(forms.Form):
    customer_email = forms.CharField(max_length = 40)
    customer_password = forms.CharField(max_length = 30)


class ChooseCarForm(forms.Form):
    car_type = forms.CharField(max_length=50)
    car_brand = forms.CharField(max_length=50)
    car_fuel_type = forms.CharField(max_length=50)
    price_per_day = forms.CharField(max_length=50)
