from django.db import models

# Create your models here.

class Event(models.Model):

    class Meta:
        db_table = 'events'

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    address = models.CharField(max_length=200)
    date = models.DateTimeField()
    date_release_tickets = models.DateField()
    number_ticket = models.IntegerField(default=10)

    def __str___(self):
        return self.title