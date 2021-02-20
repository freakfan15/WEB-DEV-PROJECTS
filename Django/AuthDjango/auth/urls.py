from django.urls import path
from auth import views

urlpatterns =[
    #path('login/', views.login), #this i used when i used the login fucntion
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view())
]