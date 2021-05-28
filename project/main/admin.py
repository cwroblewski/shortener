from django.contrib import admin

from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    readonly_fields = ("origin_url", "shortened_url")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
