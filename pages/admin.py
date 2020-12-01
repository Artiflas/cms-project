from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"/>'.format(object.photo.url))

    thumbnail.short_description = 'Bild'

    list_display = ('id', 'thumbnail', 'vorname', 'familienname',
                    'beruf', 'create_date')

    list_display_links = ('id', 'thumbnail', 'vorname', 'familienname')
    search_fields = ('vorname', 'familienname', 'beruf', 'create_date')
    list_filter = ('beruf',)


admin.site.register(Team, TeamAdmin)
