from django.contrib import admin

from .models import Slider, Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src ="{}"  width="40" />'.format(object.photo.url))

    #overwritng some lists
    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name', 'role') #helps us to search based on only roles or first names
    list_filter = ('role', )

# Register your models here.
admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)