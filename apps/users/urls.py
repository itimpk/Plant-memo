from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'  # ← namespace, important

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot/', views.reset_password_view, name='forgot'),
    # path('profile/', views.profile_view, name='profile'),
]