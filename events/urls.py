from django.contrib import admin
from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path('', views.events_page, name="index"),
    path('criar-evento/', views.get_create_event_page, name="create_event"),
    path('criar-evento_post/', views.create_event_post, name="create_event_post")
]
