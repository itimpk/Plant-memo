from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm

# Create your views here.
def signin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user provide not exists email
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/users/signin/')

        user = authenticate(username=username, password=password)

        if user is None:
            #Display error message password incorrect
            messages.error(request,'Invalid password')
            return redirect('/users/signin/')
        else:
            login(request,user)
            return redirect('/')

    return render(request, 'users/signin.html')

def logout_view(request):
    logout(request)
    messages.success(request,'Logout Success')
    return redirect('/users/signin/')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/signin/')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html',{'form':form})

def reset_password_view(request):
    pass