from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_3),
    path('index_2',views.index_2),
    path('index_3',views.index),
]