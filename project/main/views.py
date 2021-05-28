from django.shortcuts import redirect, render
from django.views import View

from .forms import UrlShortenerForm
from .models import Url


class UrlShortener(View):
    def get(self, request):
        form = UrlShortenerForm

        return render(request, "url_base.html", {"form": form})

    def post(self, request):
        form = UrlShortenerForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.shortened_url = f"{request.META['HTTP_HOST']}/{instance.uuid}"
            instance.save()

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
        return redirect(f"{Url.objects.get(id=kwargs['url_id']).origin_url}")
