from django.db import models


class Status(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)