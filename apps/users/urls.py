from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'  # ← namespace, important

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot/', views.reset_password_view, name='forgot'),
    # path('profile/', views.profile_view, name='profile'),
] 