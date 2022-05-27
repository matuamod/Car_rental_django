from django.urls import path, include
from customer import views

urlpatterns = [
    path('', views.IndexUser.as_view(), name="IndexUser"),
    path('about_site/', views.about_site, name="AboutSite"),
    path('home/', views.Home.as_view(), name="Home"),
    path('show_car/<slug:post_slug>/', views.ShowCar.as_view(), name="ShowCar"), 
    path('sign_in/',views.SignIn.as_view(), name="SignIn"),
    path('logout_customer/',views.logout_customer,name="LogoutCustomer"),    
    path('registration/',views.Registration.as_view(), name="Registration"),
    # path('search_car/', views.ChooseCar.as_view(), name='ChooseCar'),
    # path('logined_customer/', views.LoginedCustomer.as_view(),name="LoginedCustomer"),
    # path('registrated_customer/', views.registrated_customer,name="RegistratedCustomer"),
    path('customer_profile/', views.customer_profile,name="CustomerProfile")
]