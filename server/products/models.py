from django.db import models

# Create your models here.
class CustomProduct(models.Model):
    title = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=1000,
        blank=True
    )