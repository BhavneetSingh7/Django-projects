from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ApiToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    key = models.CharField(max_length=30, unique =True, blank=False, null=True)
    og_key = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + "'s API Token"