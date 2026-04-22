from django.shortcuts import render,redirect
from .forms import PlantForm,GroupForm
from .models import Group,Plant

# Create your views here.

def home_view(request):
    plants = Plant.objects.filter(user=request.user)
    groups = Group.objects.filter(user=request.user)
    return render(request,"plants/overviews.html",{"groups":groups,"plants":plants})

def add_group(request):
    if request.method == "POST":
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group = group_form.save(commit=False)
            group.user = request.user
            group_form.save()
            return redirect('/plants/home')
    else:
        group_form = GroupForm()
    return render(request,"plants/add_group.html",{'form':group_form})

def add_plant(request):
    if request.method == "POST":
        form = PlantForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.user = request.user
            plant.save()
            return redirect('/plants/home')
    else:
        form = PlantForm(request.user)  # pass user here
    return render(request,"plants/add_plant.html",{'form':form})
