from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default='USER')
    photo = models.ImageField(upload_to='user_photo',default='User.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=70, null=True)

    def __str__(self):
        return self.username