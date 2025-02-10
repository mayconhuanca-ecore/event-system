from django.contrib import admin
from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path('', views.events_page, name="index"),
]
