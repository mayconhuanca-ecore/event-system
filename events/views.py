from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
# Create your views here.

def events_page(request):
    events_list = Event.objects.all()
    return render(request, "events/events.html", {"events": events_list})