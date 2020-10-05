from django.db import models


# Create your models here.
class TodoBoard(models.Model):
    task = models.CharField(max_length=100)
    status = models.BooleanField(default=0)
