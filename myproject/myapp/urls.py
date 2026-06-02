from django.urls import path 
from .views import display, morning_messsage, noon_messsage, evening_messsage

urlpatterns = [
    path('display/', display, name='display'),
    path('morning/', morning_messsage),
    path('noon/', noon_messsage),
    path('evening/', evening_messsage),
]

