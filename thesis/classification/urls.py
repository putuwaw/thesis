from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("report", views.report, name="report"),
    path("predict", views.predict, name="predict"),
    path("about", views.about, name="about"),
    path("api/predict/", views.api_predict, name="api-predict")
]
