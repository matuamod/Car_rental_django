from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_fname', 'customer_lname', 'customer_gender', 'customer_address', 'customer_city')
    list_display_links = ('id', 'customer_fname', 'customer_gender', 'customer_city')
    search_fields = (('id', 'customer_fname', 'customer_gender', 'customer_city'))

admin.site.register(Customer, CustomerAdmin)
