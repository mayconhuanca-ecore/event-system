from django.contrib import admin
from .models import Event, Registration, Ticket, Category

# Register your models here.

admin.site.register(Event);
admin.site.register(Registration);
admin.site.register(Ticket);
admin.site.register(Category);