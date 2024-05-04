from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_topics, name='list_topics'),
    path('headlines/<int:pk>/', views.list_headlines, name='headlines'),
    path('article/<int:pk>/', views.details, name='article_details')
]
