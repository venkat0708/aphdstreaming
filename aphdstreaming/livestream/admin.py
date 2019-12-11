from django.contrib import admin

# Register your models here.
from .models import Event, Image

class ImageInline(admin.TabularInline):
    model = Image

class EventAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
    list_display  = [f.name for f in Event._meta.fields]
    list_filter = ('status',)
admin.site.register(Event,EventAdmin)
