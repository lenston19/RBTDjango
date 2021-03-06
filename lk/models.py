from django.db import models

class User(models.Model):
    username = models.CharField(
        max_length=50,
        verbose_name='',
        unique=True,
    )

    def __str__(self):
        return f"{self.username}"
