from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_home, name="dashboard-home"),
    path("home/", views.dashboard_home, name="dashboard-home"),
    path("training/", views.dashboard_training, name="dashboard-training"),
    path("testing/", views.dashboard_testing, name="dashboard-testing"),
    path("report/", views.dashboard_report, name="dashboard-report"),
    # data
    path("data/", views.dashboard_data, name="dashboard-data"),
    path(
        "data/training/", views.dashboard_data_training, name="dashboard-data-training"
    ),
    path("data/testing/", views.dashboard_data_testing, name="dashboard-data-testing"),
    path("data/download", views.download_data, name="download-data"),
    # temp delete all dataset
    path("data/delete", views.delete_all_data, name="delete-all-dataset"),
]
