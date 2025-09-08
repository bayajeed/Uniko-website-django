from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="setting_home"),
]
