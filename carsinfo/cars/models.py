from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Car(models.Model):
    """Модель машины."""

    make = models.CharField(
        max_length=32
    )
    model = models.CharField(
        max_length=32
    )
    year = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    """Модель комментария."""

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)