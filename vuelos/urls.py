from django.urls import path
from . import views

urlpatterns = [
    path('', views.vuelo_list, name='vuelo_list'),
]
