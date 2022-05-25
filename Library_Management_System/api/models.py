from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=70, default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ADMIN = "admin"
    USER =  "user"
    USER_TYPE = (
        (ADMIN, "Admin"),
        (USER, "User")
    )
    role = models.CharField(null=True, blank=True, choices=USER_TYPE, max_length=7, default=ADMIN)