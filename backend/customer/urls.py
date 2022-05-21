from django.urls import path, include
from customer import views

urlpatterns = [
    path('index_user/', views.index_user,name="Index"),
    path('sign_in/',views.sign_in,name="SignIn"),
    path('log_out/',views.log_out,name="Logout"),    
    path('registration/',views.registration,name="Register"),
]