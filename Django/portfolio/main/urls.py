from django.urls import path
from main import views

urlpatterns =[
    path('projects/', views.projects, name='projects'),
    path('blogs/', views.blogs, name='blogs'),
    path('', views.index, name = 'index'),
]