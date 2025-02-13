from django.contrib import admin
from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path('', views.events_page, name="index"),
    path('criar-evento/', views.create_event, name="create_event")
]
