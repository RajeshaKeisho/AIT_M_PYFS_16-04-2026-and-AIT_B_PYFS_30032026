from django.shortcuts import render
from .models import EmployeeProxy, CustomerProxy
from django.views.generic import ListView
# Create your views here.

class EmployeeListView(ListView):
    model = EmployeeProxy
    template_name = "people/employee_list.html"
    context_object_name = 'employees'

class CustomerListView(ListView):
    model = CustomerProxy
    template_name = "people/customer_list.html"
    context_object_name = 'customers'
    