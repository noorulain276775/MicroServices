from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator



class User(AbstractUser):
    pass


class AllProducts(models.Model):
    ELECTRONICS = 'EL'
    CLOTHING = 'CL'
    HOMEACCESSORIES = 'HA'
    HEALTH = 'HE'
    BEAUTY = 'BE'
    CATEGORIES = [
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (HOMEACCESSORIES, 'HomeAccessories'),
        (HEALTH, 'Health'),
        (BEAUTY, 'Beauty'),
    ]
    name = models.CharField(max_length=100, blank=False,
                            null=False, verbose_name="Name")
    category = models.CharField(max_length=2,
                                choices=CATEGORIES,
                                default=ELECTRONICS, verbose_name="Category")
    brand = models.CharField(max_length=50, verbose_name="Brand")
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=20, verbose_name="Quantity")
    rating = models.FloatField(
    validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name