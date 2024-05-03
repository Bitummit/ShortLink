from django.db import models

class Link(models.Model):
    full_link = models.TextField()
    short_link = models.CharField(max_length=128)

    class Meta:
        