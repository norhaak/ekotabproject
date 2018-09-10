from django.contrib import admin
from django.urls import path
from . import views
from ekotab.views import StudentCreate, StudentDelete, StudentUpdate

app_name = 'ekotab'
urlpatterns = [
    path('', views.student_list, name='list'),
    path('student/add', StudentCreate.as_view(), name='student-add'),
    path('student/<slug:slug>/update', StudentUpdate.as_view(), name='student-update'),
    path('student/<slug:slug>/delete', StudentDelete.as_view(), name='student-delete'),
    path('student/<slug:student_slug>', views.student_detail, name='detail'),
]
