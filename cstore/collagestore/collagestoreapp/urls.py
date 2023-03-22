from django.urls import path

from . import views

app_name = 'collagestoreapp'

urlpatterns = [
    path('contact',views.contact,name="contact"),
    path('',views.home1,name="home1"),
    path('order/', views.place_order.as_view(), name='order'),
    path('ajax/get_courses/', views.get_courses, name='ajax_get_courses'),
    path('sucess/',views.sucess,name='sucess')

]