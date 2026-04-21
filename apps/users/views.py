from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user provide not exists email
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/users/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            #Display error message password incorrect
            messages.error(request,'Invalid password')
            return redirect('/users/login/')
        else:
            login(request,user)
            redirect('/')

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'Logout Success')
    return redirect('/users/login/')

def register_view(request):
    pass

def reset_password_view(request):
    pass