from django.db import models

# Create your models here.
class Link(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.link