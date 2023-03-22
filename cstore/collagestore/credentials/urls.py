from . import views
from django.urls import path

app_name = 'credentials'
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('form', views.form, name='form'),
    ]