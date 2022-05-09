from django.urls import path, include

urlpatterns = [
    path('cars/', include('Car.urls')),
]
