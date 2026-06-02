from django.urls import path
from .views import my_view, greeting, message

urlpatterns = [
    path("my_view/", my_view),
    path("greeting/", greeting),
    path("message/", message),
]
