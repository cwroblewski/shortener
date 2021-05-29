import uuid

from django.db import models

# Create your models here.
from project import settings


class Url(models.Model):
    origin_url = models.TextField(verbose_name="origin url", unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.uuid)

    @property
    def shortened_url(self):
        return f"{settings.DOMAIN}/{self.uuid}"
