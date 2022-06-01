from urllib import response
from django.test import TestCase
from django.urls import reverse
from .models import Customer
from car.models import Car
import json

class TestCustomerViews(TestCase):

    def test_index_user_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_about_site_page(self):
        response = self.client.get('/about_site/')
        self.assertEqual(response.status_code, 200)


    def test_home_page(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)


    def test_show_car_page(self):
        cars = Car.objects.all()

        for car in cars:
            response = self.client.get(f'/show_car/{car.slug}/')
            self.assertEqual(response.status_code, 200)


    def test_sign_in_page(self):
        response = self.client.get('/sign_in/')
        self.assertEqual(response.status_code, 200)


    def test_registration_page(self):
        response = self.client.get('/registration/')
        self.assertEqual(response.status_code, 200)


    def test_logout_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_profile_page(self):
        customers = Customer.objects.all()

        for customer in customers:
            response = self.client.get(f'/customer_profile/{customer.pk}/')
            self.assertEqual(response.status_code, 200)


    def test_availability_page(self):
        cars = Car.objects.all()

        for car in cars:
            response = self.client.get(f'/show_car/{car.pk}/')
            self.assertEqual(response.status_code, 200)






