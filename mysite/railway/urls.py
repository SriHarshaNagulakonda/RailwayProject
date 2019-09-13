from django.urls import path

from . import views

app_name='railway'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_city/',views.add_city,name='add_city'),
    path('insert_city/',views.insert_city,name='insert_city'),
]
