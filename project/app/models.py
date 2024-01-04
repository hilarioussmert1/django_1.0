from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='product'
    )
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(validators=[MinValueValidator(0.0)],)

    def __str__(self):
        return f'{self.product_name.title()}: {self.description}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories', blank=True)

    def __str__(self):
        return self.name.title()
