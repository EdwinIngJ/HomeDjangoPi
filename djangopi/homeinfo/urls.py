from django.urls import path
from . import views

app_name = "homeinfo"

urlpatterns = [
    path("", views.DashBoard.as_view(), name="dashboard"),
    path("update_toggle/", views.update_toggle, name="update_toggle"),
    path("update_page/", views.update_page, name="update_page"),
]

