from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Event, Category
from django.urls import reverse
# Create your views here.

def events_page(request):
    events_list = Event.objects.all()
    return render(request, "events/events.html", {"events": events_list})

def get_create_event_page(request):
    categories = Category.objects.all()
    return render(request, "events/create-event.html", {"categories": categories})

def create_event_post(request):
    return HttpResponseRedirect(reverse("events:index"))