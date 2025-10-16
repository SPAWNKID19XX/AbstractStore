from django.db import models

# Create your models here.
class CustomProduct(models.Model):
    title = models.CharField(
        max_length=50
    )