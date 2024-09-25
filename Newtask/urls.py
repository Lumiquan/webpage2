from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.group, name='group'),
    path('grouplist/', views.grouplist, name='grouplist'),
]