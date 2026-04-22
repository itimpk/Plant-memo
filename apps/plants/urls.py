from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'plants'  # ← namespace, important

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('home/group/', views.add_group, name='add_group'),
    path('home/plant/', views.add_plant, name='add_plant'),

]