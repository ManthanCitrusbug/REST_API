from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=70, unique=True, default=None, blank=True, null=True)
    user = models.ManyToManyField(User)

    # def __str__(self):
    #     return self.name