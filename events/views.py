from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Event, Category
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .forms import CreateEventForm

# Create your views here.

def events_page(request):
    events_list = Event.objects.all()
    return render(request, "events/events.html", {"events": events_list})

def create_event(request):
    
    categories = Category.objects.all()

    if request.method == "POST":
        event_form = CreateEventForm(request.POST)

        # TODO: USER SHOULD BE LOGGED
        user = User.objects.get(pk=1);
            
        if event_form.is_valid():

            categories = Category.objects.filter(id__in=event_form.cleaned_data["categories"])

            if not categories.exists():
                
                return render(
                    request,
                    "events/create-event.html", 
                    {
                        "category_error_message":"Selecione uma categoria valida!"
                    }
                )

            new_event = Event(
                title=event_form.cleaned_data["title"],
                description=event_form.cleaned_data["description"],
                address=event_form.cleaned_data["address"],
                date=event_form.cleaned_data["date"],
                date_release_tickets=timezone.now(),
                number_ticket=event_form.cleaned_data["quantity"],
                user=user,
            );

            new_event.save()

            new_event.categories.set(categories)
        
            return HttpResponseRedirect(reverse("events:index"))
    
    if request.method == "GET":
        
        context = {
            "form_create_event": CreateEventForm(categories=categories)
        }

        return render(request, "events/create-event.html", context)

    return events_page(request);