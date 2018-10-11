from django.urls import path
from meetups_list import views


urlpatterns = [
    path('', views.index, name='index'),
]
