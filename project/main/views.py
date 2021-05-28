from django.shortcuts import (
    render,
    redirect
)
from django.views import View

from .forms import UrlShortenerForm
from .models import Url


class UrlShortener(View):

    def get(self, request):
        form = UrlShortenerForm
        return render(request, 'url_base.html', {'form': form})

    def post(self, request):
        form = UrlShortenerForm(request.POST)
        if form.is_valid():
            origin_url = form.cleaned_data['origin_url']
            Url.objects.create(origin_url=origin_url)
            last_id = Url.objects.latest('id')
            Url.objects.filter(id=last_id.id).update(shortened_url='localhost:8000/{}/'.format(last_id.id))
            record = Url.objects.get(id=last_id.id)

            return render(request, 'url_base.html', {'origin_url': record.origin_url,
                                                     'shortened_url': record.shortened_url})


class OriginUrlView(View):
    def get(self, request, url_id):
        id = url_id
        record = Url.objects.get(id=id)
        url = record.origin_url
        return redirect('{}'.format(url))
