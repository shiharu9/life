from django.contrib import admin
from .models import Event, Period
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'period', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'period')


admin.site.register(Event, EventAdmin)
admin.site.register(Period)
