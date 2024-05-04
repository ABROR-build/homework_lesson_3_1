from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_subjects, name='list_subjects'),
    path('lessons/<int:pk>/', views.list_lessons, name='list_lessons'),
    path('lesson/<int:pk>/', views.get_lesson, name='get_lesson')

]
