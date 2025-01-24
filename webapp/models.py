import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Address(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'addresses'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.country},{self.city},{self.name}'


STATUS_CHOICES = [
    ('waiting', 'Ожидание'),
    ('received', 'У нас'),
    ('on way', 'В пути'),
    ('in stock', 'На складe'),
    ('delivered', 'Получено'),
]


class Package(models.Model):
    address = models.ForeignKey('webapp.Address', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=30)
    weight = models.FloatField()
    link = models.URLField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def price(self):
        return self.weight * 3.1

    class Meta:
        db_table = 'packages'
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return f'{self.title} {self.status}'

    def save(self, *args, **kwargs):
        self.tracking_number = uuid.uuid4()
        return super().save(*args, **kwargs)
