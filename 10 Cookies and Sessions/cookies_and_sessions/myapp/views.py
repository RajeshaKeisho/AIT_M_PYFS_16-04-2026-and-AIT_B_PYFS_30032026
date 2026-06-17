from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages

# Create your views here.

USERS = {
    'admin':"password123",
    'user':'user1233'
}

def home(request):
    username = request.session.get("username", "Guest")
    theme = request.COOKIES.get("theme", "light")
    last_activity = request.session.get("last_activity", "No activity recorded")

    return render(request, 'home.html', {'username':username, 'theme':theme, 'last_activity':last_activity})

def set_cookie(request):
    response = HttpResponse("Cookie has been set!")
    response.set_cookie("username", "Abdul", max_age=60)
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', "Guest")
    return HttpResponse(f"Hello, Welcome {username}")

def set_session(request):
    request.session["user_id"] = 12345
    request.session["last_activity"] = str(timezone.now())
    return HttpResponse(f"Session has been set!")

def get_session(request):
    user_id = request.session.get("user_id", "NO LoggedIn User")
    last_actitity = request.session.get("last_activity", 'No Activity recorded')
    return HttpResponse(f"User ID: {user_id}, Last Activity: {last_actitity}")

def clear_session(request):
    request.session.flush()
    return HttpResponse("Session has been cleared!")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username in USERS and USERS[username] == password:
            request.session["username"] = username
            request.session["last_activity"] = str(timezone.now())
            messages.success(request, "Login Successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password")
    return render(request, "login.html")


def logout(request):
    request.session.flush()
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def set_theme(request):
    if request.method == 'POST':
        theme = request.POST.get('theme')
        response = redirect('home')
        response.set_cookie('theme', theme, max_age=30 * 24 * 60 * 60)  # Cookie expires in 30 days
        messages.success(request, f'The theme has been set to {theme}.')
        return response
    return render(request, 'set_theme.html')


def protected_view(request):
    if 'username' not in request.session:
        messages.error(request, 'You must be logged in to access this page.')
        return redirect('login')
    return HttpResponse("This is a protected page. Only logged-in users can see this.")

