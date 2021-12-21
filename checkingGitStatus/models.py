from django.db import models


class Repo(models.Model):
    name = models.CharField(max_length=100)
    is_private = models.BooleanField(default=True)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.name
