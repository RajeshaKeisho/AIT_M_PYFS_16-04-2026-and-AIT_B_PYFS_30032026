from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    time = datetime.datetime.now()
    name = "Jayanthi"
    rollno = 101
    age = 21
    marks = 90
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    my_dict = {'insert_time':formatted_time, 'name':name, 'rollno':rollno, 'age':age, 'marks':marks}

    return render(request, 'wish.html', my_dict)


def wish1(request):
    time = datetime.datetime.now()
    msg = " Hello friends!! Very Very Good"
    h = int(time.strftime("%H"))
    if h<12:
        msg+=" MORNING!" 
    elif h<16:
        msg+= " AFTERNOON"
    elif h<21:
        msg+= " EVENING"
    else:
        msg = "Hello Guest, Good Night!!!"
    my_dict = {"insert_time":time, "insert_data":msg}
    return render(request, 'myapp/wish1.html', context=my_dict)


def greet(request):
    now = datetime.datetime.now()
    current_time = now.strftime("%H %M %S")

    if now.hour < 12:
        greeting = "Good morning!"
    elif now.hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    return render(request, 'greet.html', {'greeting':greeting, 'current_time':current_time})

