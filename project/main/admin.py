from django.contrib import admin

from .models import Url


@admin.register(Url)
class Url_s_Admin(admin.ModelAdmin):
    list_display = ("id", "origin_url", "shortened_url")
