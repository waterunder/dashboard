from dive.models import Dive
from django.contrib import admin


class DiveAdmin(admin.ModelAdmin):
    list_display = ('date', 'lat', 'lon', 'visibility', 'bottom_time', 'diver')
    list_filter = ('date',)

    def diver(self, obj):
        return obj.created_by.email


admin.site.register(Dive, DiveAdmin)
