from django.contrib import admin
from django.urls import (
    path,
    re_path
)

from main.views import (
    UrlShortener,
    OriginUrlView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UrlShortener.as_view()),
    re_path('(?P<url_id>(\d)+)/', OriginUrlView.as_view())
]
