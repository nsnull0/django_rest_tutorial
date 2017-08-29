from django.contrib import admin

from casino_finder.models import Casino


@admin.register(Casino)
class CasinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'modified_at', 'created_at')
