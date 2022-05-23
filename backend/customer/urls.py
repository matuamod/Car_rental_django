from django.urls import path, include
from customer import views

urlpatterns = [
    path('', views.index_user,name="Index"),
    path('home/', views.home, name="Home"),
    path('sign_in/',views.sign_in,name="SignIn"),
    path('logout_customer/',views.logout_customer,name="LogoutCustomer"),    
    path('registration/',views.registration,name="Register"),
    path('logined_customer/', views.logined_customer,name="LoginedCustomer"),
    path('registrated_customer/', views.registrated_customer,name="RegistratedCustomer"),
    path('customer_profile/', views.customer_profile,name="CustomerProfile")
]