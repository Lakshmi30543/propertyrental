from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLES = (
        ('tenant', 'Tenant'),
        ('owner', 'Owner'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use Django's password hashing for security
    role = models.CharField(max_length=10, choices=ROLES)  # Add role field

    def __str__(self):
        return f'{self.name} - {self.role}'


