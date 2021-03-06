from django.conf import settings
from django.db import models
from django.utils import timezone


class Affiche(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title