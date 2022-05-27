from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_brand', 'car_model', 'car_fuel_type', 'car_color', 'count_of_seats', 'car_plate', 'price_per_day')
    list_display_links = ('id', 'car_plate', 'price_per_day')
    search_fields = ('id', 'car_plate') 
    prepopulated_fields = {'slug': ('car_brand', 'car_model')}

admin.site.register(Car, CarAdmin)
