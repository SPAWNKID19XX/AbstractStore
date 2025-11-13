from django.db import models
from users.models import CustomUser


# Create your models here.
class CustomProduct(models.Model):
    title = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=1000,
        blank=True
    )


class ProductComments(models.Model):
    class RAITING_VALUES(models.IntegerChoices):
        ONE = 1, "★☆☆☆☆"
        TWO = 2, "★★☆☆☆"
        THREE = 3, "★★★☆☆"
        FOUR = 4, "★★★★☆"
        FIVE = 5, "★★★★★"


    class Meta:
        indexes = [
            models.Index(fields=["product"]),
            models.Index(fields=["user", "product"]),
        ]

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        CustomProduct,
        on_delete=models.CASCADE
    )

    comment = models.TextField(
        max_length=2000
    )

    rating = models.CharField(choices=RAITING_VALUES.choices)

    published_at = models.DateTimeField('Published at:',auto_now_add=True)
    updated_at = models.DateTimeField('Updated at:', null=True, blank=True)
