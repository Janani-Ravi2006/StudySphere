from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('resource/<int:resource_id>/', views.resource_detail, name='resource_detail'),
]
