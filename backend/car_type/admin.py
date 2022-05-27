from django.contrib import admin
from .models import Car_Type

class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_type')
    list_display_links = ('id', )
    search_fields = ('id', )

admin.site.register(Car_Type, CarTypeAdmin)

