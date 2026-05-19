from django.urls import path
from .views import add_job, update_job, delete_job

urlpatterns = [

    path('add/', add_job, name='add_job'),

    path('update/<int:id>/', update_job, name='update_job'),

    path('delete/<int:id>/', delete_job, name='delete_job'),
]