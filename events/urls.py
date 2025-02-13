from django.contrib import admin
from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path('', views.events_page, name="index"),
    path('criar-evento/', views.create_event, name="create_event"),
    path('<int:event_id>/', views.event_detail, name="event_details"),
    path('<int:event_id>/buy', views.buy_ticket, name="buy_ticket")
]
