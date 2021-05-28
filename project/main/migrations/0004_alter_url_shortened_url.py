# Generated by Django 3.2.3 on 2021-05-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_url_shortened_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="shortened_url",
            field=models.CharField(
                editable=False, max_length=128, verbose_name="shortened url"
            ),
        ),
    ]
