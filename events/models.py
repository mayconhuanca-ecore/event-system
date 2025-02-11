from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):

    class Meta:
        db_table = "categories"

    name = models.CharField(200)

class Event(models.Model):

    class Meta:
        db_table = 'events'

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    address = models.CharField(max_length=200)
    date = models.DateTimeField()
    date_release_tickets = models.DateField()
    number_ticket = models.IntegerField(default=10)
    categories = models.ManyToManyField(Category, related_name="events")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")

    def __str___(self):
        return self.title

class Registration(models.Model):

    class Meta:
        db_table = 'registrations'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class Ticket(models.Model):

    class Meta:
        db_table = 'tickets'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    code = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

