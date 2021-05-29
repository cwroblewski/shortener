from django.shortcuts import redirect, render
from django.views import View

from project import settings

from .forms import UrlShortenerForm
from .models import Url


class UrlShortener(View):
    def get(self, request):
        form = UrlShortenerForm

        return render(request, "url_base.html", {"form": form})

    def post(self, request):
        form = UrlShortenerForm(request.POST)

        if form.is_valid():
            instance = form.save()

            return render(
                request,
                "url_base.html",
                {
                    "origin_url": instance.origin_url,
                    "shortened_url": instance.shortened_url,
                },
            )

        return render(request, "url_base.html", {"form": form})


class OriginUrlView(View):
    def get(self, request, **kwargs):
        return redirect(f"{Url.objects.get(uuid=kwargs['uuid']).origin_url}")
