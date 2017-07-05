__author__ = 'Galleani'

from django.contrib import admin
from core.models import Interaction

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ['id', 'input', 'output']
    search_fields = ['client', 'input']