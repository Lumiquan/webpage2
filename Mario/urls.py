from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.squad, name='squad'),
    path('Mariolist/', views.Mariolist, name='Mariolist'),
]