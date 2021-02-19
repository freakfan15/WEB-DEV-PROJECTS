from django.urls import path
from django.urls.resolvers import URLPattern

from main import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('college/<int:pk>', views.CollegeDetail.as_view(), name='college'),
    path('college/', views.CollegeList.as_view()),
    path('create_college/', views.CreateCollege.as_view()),
    path('update_college/<int:pk>', views.UpdateCollege.as_view()),
    path('create_student/', views.CreateStudent.as_view()),
    path('delete_student/<int:pk>', views.DeleteStudent.as_view())
    
]