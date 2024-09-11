from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard-home'),
    path('home/', views.dashboard_home, name='dashboard-home'),
    path('data/', views.dashboard_data, name='dashboard-data'),
    path('training/', views.dashboard_training, name='dashboard-training'),
    path('testing/', views.dashboard_testing, name='dashboard-testing'),
]
