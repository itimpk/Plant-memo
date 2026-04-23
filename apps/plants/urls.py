from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'plants'  # ← namespace, important

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('group/create', views.group_create, name='group_create'),
    path('plant/create', views.plant_create, name='plant_create'),
    path('plant/<int:plant_id>', views.plant_detail, name='plant_detail'),
    path('plant/update/<int:plant_id>', views.plant_update, name='plant_update'),
    path('plant/delete/<int:plant_id>', views.plant_delete, name='plant_delete'),

]