from django.urls import path
from . import views

app_name = "homeinfo"

urlpatterns = [
    path("", views.DashBoard.as_view(), name="dashboard"),
]

