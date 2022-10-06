from django.db import models

# Create your models here.
class Creds(models.Model):
    email_id = models.EmailField()
    verified = models.BooleanField(default=False)
    verify_key = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Email: '+self.email_id