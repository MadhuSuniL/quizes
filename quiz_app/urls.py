from django.urls import path
from .views import *

urlpatterns = (
    path('all/',QuizGetAllView.as_view()),    
    path('<pk>/',QuizRetrieveView.as_view()),    
    path('<pk>/answer',QuizAnswerView.as_view()),    
    path('all/<str:status>/',QuizStatusWiseView.as_view()),    
    path('create',QuizCreateView.as_view()),    
)