from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('flights/', include('flights.urls', namespace='flights')),
]