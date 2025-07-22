from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name= 'home'),
    path('gpa/', views.gpa_form_view, name= 'gpa'),
    path('gpa/subjects/<int:count>/', views.subject_input_view),
    path('cgpa/', views.cgpa_form_view, name = 'cgpa'),
    path('cgpa/semesters/<int:count>/', views.semester_input_view),
]
