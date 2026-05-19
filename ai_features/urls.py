from django.urls import path
from .views import interview_questions

urlpatterns = [

    path('', interview_questions, name='interview_questions'),
]