from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category, Ticket
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

from .forms import CreateEventForm, CustomLoginForm, SignUpForm

# Create your views here.

def events_page(request):
    events_list = Event.objects.all()
    return render(request, "events/events.html", {
        "events": events_list, 
        "user": request.user
    })

@login_required
def create_event(request):

    categories = Category.objects.all()

    if request.method == "POST":
        event_form = CreateEventForm(request.POST, categories=categories)

        user = request.user
            
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

            date_release_ticket = event_form.cleaned_data.get("date_release_tickets", timezone.now())

            new_event = Event(
                title=event_form.cleaned_data["title"],
                description=event_form.cleaned_data["description"],
                address=event_form.cleaned_data["address"],
                date=event_form.cleaned_data["date"],
                date_release_tickets= date_release_ticket,
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

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    current_date = timezone.now().date()
    
    tickets_sold = Ticket.objects.filter(event=event).count()
    quantity_tickets_available = event.number_ticket - tickets_sold;
    
    context = { 
        "event": event,
        "current_date": current_date,
        "can_buy": there_is_ticket_availabe(event_id),
        "tickets_available": quantity_tickets_available
    }

    return render(request, "events/detail.html", context)

@login_required
def buy_ticket(request, event_id):
    user = request.user
    event = get_object_or_404(Event, pk=event_id)

    if there_is_ticket_availabe(event_id=event_id):
        ticket = Ticket(user=user, event=event, code="AAAA", created_at=timezone.now());
        ticket.save()

        return render(request, "events/buy-ticket.html", {
            "event": event,
            "ticket": ticket
        })
    
    else:
        return render(request, "events/no-ticket.html", {"event": event})


def login_page(request): 
    if request.method == "POST":
        login_form = CustomLoginForm(request=request, data=request.POST)
        
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("/events")
        else:
            return render(request, "accounts/login.html", {"login_form": login_form})


    else:
        login_form = CustomLoginForm()
        return render(request, "accounts/login.html", {"login_form": login_form})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/events")
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("/events") 


def there_is_ticket_availabe(event_id):
    event = get_object_or_404(Event, pk=event_id)
    quantity_tickets_sold = Ticket.objects.filter(event=event).count()

    if event.number_ticket <= quantity_tickets_sold:
        return False
    
    return True

