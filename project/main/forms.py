from django import forms
from django.core.validators import URLValidator

from .models import Url


class UrlShortenerForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ["origin_url"]

    def clean(self):
        cleaned_data = super().clean()
        validate = URLValidator()
        try:
            validate(
                cleaned_data["origin_url"],
            )
        except Exception:
            self.add_error(
                "origin_url",
                "This is not correct URL. Check format, example: 'http://nameless-sierra-69417.herokuapp.com/'",
            )
        return cleaned_data
