# Generated by Django 3.2.7 on 2021-09-16 13:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='passenger',
            field=models.ManyToManyField(blank=True, related_name='flights', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Passenger',
        ),
    ]
