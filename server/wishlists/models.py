from django.db import models
from users.models import CustomUser
from products.models import CustomProduct

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        CustomProduct,
        on_delete=models.CASCADE
    )
