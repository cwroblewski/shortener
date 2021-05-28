from django.contrib import admin
from django.urls import path

from main.views import OriginUrlView, UrlShortener

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", UrlShortener.as_view()),
    path("<int:url_id>/", OriginUrlView.as_view()),
]
