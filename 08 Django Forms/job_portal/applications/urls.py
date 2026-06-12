from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.job_application_view, name='job_application'),
    path('contact/', views.contact_view, name='contact'),
]
