from django.shortcuts import get_object_or_404, render,redirect
from .forms import PlantForm,GroupForm
from .models import Group,Plant,PlantLog

# Create your views here.

def home_view(request):
    plants = Plant.objects.filter(user=request.user).order_by('id')
    groups = Group.objects.filter(user=request.user).order_by('id')
    return render(request,"plants/home.html",{"groups":groups,"plants":plants})

def group_create(request):
    if request.method == "POST":
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group = group_form.save(commit=False)
            group.user = request.user
            group_form.save()
            return redirect('/plants/home')
    else:
        group_form = GroupForm()
    return render(request,"plants/group_create.html",{'form':group_form})

def group_update(request,id):
    group = get_object_or_404(Group,id=id)
    if request.method == "POST":
        form = GroupForm(request.POST,instance=group)
        if form.is_valid():
            group = form.save()
            return redirect("/plants/home")
    else:
        form = GroupForm(instance=group)
    return render(request,"plants/group_update.html",{"form":form,"group":group})

def group_delete(request,id):
    group = Group.objects.get(id=id)
    group.delete()
    return redirect('/plants/home')

def plant_create(request):
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES,user=request.user)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.user = request.user
            plant.save()
            return redirect('/plants/home')
    else:
        form = PlantForm(user=request.user)  
    return render(request,"plants/plant_create.html",{'form':form})

def plant_detail(request,plant_id):
    plant = Plant.objects.get(id = plant_id)
    logs = PlantLog.objects.filter(user=request.user).order_by('-created_at')
    return render(request,"plants/plant_detail.html",{"plant":plant,"logs":logs})

def plant_update(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    
    if request.method == "POST":
        # CRITICAL: You must pass user=request.user here too!
        form = PlantForm(request.POST, request.FILES, instance=plant, user=request.user)
        
        if form.is_valid():
            form.save() 
            return redirect(f"/plants/plant/{plant.id}")
    else:
        # This part was already correct
        form = PlantForm(instance=plant, user=request.user)
        
    return render(request, "plants/plant_update.html", {"form": form, "plant": plant})

def plant_delete(request,plant_id):
    plant = Plant.objects.get(id=plant_id)
    plant.delete()
    return redirect('/plants/home')


def log_add(request, plant_id):
    if request.method == "POST":
        plant = get_object_or_404(Plant, id=plant_id)
        
        # Grab data from the Modal form fields
        action = request.POST.get('action')
        note = request.POST.get('note')
        
        # Create the log entry
        PlantLog.objects.create(
            user=request.user,
            plant=plant,
            action=action,
            note=note
        )

    return redirect(request.META.get('HTTP_REFERER', '/'))