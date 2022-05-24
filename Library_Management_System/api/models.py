from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=70, default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    Admin = 1
    User = 2
    USER_TYPE = (
        (Admin, "Admin"),
        (User, "User")
    )
    role = models.CharField(null=True, blank=True, choices=USER_TYPE, max_length=1)



# class ISAdmin(AbstractUser):

#     USER_TYPE = (
#         ("A", "Admin"),
#         ("U", "User")
#     )
#     is_admin = models.CharField(max_length=10, choices=USER_TYPE)

    # def __str__(self):
    #     return self.name