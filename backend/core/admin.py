from django.contrib import admin
from .models import Locations


@admin.register(Locations)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'place', 'place', 'email')