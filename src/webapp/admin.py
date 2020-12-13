from django.contrib import admin

from webapp.models import Musician


class MusicianAdmin(admin.ModelAdmin):
    list_display = ['author']
    exclude = []
    search_fields = ['author']


admin.site.register(Musician, MusicianAdmin)
