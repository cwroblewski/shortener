import uuid

from django.db import models

# Create your models here.


class Url(models.Model):
    origin_url = models.TextField(verbose_name="origin url", unique=True)
    shortened_url = models.CharField(
        verbose_name="shortened url", max_length=128, editable=False
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.uuid)
