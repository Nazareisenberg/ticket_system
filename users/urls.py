from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # Регистрация
    path('register/', views.register, name='register'),
    # Вход
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Выход
    path('logout/', views.logout_view, name='logout'),
   
]
