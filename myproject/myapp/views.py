# from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def display(request):
    s = "<h1> Hello, Students! Welcome to Django Class!</h1>"
    return HttpResponse(s)


def morning_messsage(request):
    time = datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1> Hello, Good Morning! Now the time is " + formatted_time + "</h1>")

def noon_messsage(request):
    time = datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1> Hello, Good Afternoon! Now the time is " + formatted_time + "</h1>")

def evening_messsage(request):
    time = datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1> Hello, Good Evening! Now the time is " + formatted_time + "</h1>")
