from django.db import models
import random
from Shortlink.settings import (
    CHARACTERS_FOR_LINKS, 
    LINK_LENGTH
)
class Link(models.Model):
    full_link = models.TextField()
    short_link = models.CharField(max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.short_link:
            while True:
                generated_link = "".join(
                    random.choices(CHARACTERS_FOR_LINKS, k=LINK_LENGTH)
                )
                if not Link.objects.filter(short_link=generated_link).exists():
                    self.short_link = generated_link
                    break
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_link} -> {self.short_link}'
    
    def __repr__(self):
        return self.__str__()