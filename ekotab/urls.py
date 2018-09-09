from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ekotab'
urlpatterns = [
    path('', views.student_list, name='list'),
    path('<slug:student_slug>', views.student_detail, name='detail'),
]
