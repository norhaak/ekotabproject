from django.contrib import admin
from django.urls import path
from . import views
from ekotab.views import StudentCreate, StudentDelete, StudentUpdate, StepCreate, StepUpdate, StepDelete

app_name = 'ekotab'
urlpatterns = [
    path('', views.student_list, name='list'),
    path('student/add', StudentCreate.as_view(), name='student-add'),
    path('student/<slug:slug>/update', StudentUpdate.as_view(), name='student-update'),
    path('student/<slug:slug>/delete', StudentDelete.as_view(), name='student-delete'),
    path('step/add', StepCreate.as_view(), name='step-add'),
    path('step/<slug:slug>/update', StepUpdate.as_view(), name='step-update'),
    path('step/<slug:slug>/delete', StepDelete.as_view(), name='step-delete'),
    path('student/<slug:student_slug>', views.student_detail, name='detail'),
]
