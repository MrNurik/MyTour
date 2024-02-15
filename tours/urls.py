from . import views
from django.urls import path

app_name= 'tours'

urlpatterns = [
    path('', views.base, name='main'),
    path('booking/', views.booking, name='booking'),
    path('booking/readmore', views.readmore, name='readmore'),
    path('register/', views.register, name='register'),
]
