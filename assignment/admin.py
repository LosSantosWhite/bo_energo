from django.contrib import admin
from assignment.models import Color, Item


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["color", "number"]
