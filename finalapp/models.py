from django.db import models


class UserProfile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    english_level = models.CharField(max_length=20)

    def __str__(self):
        return self.email

