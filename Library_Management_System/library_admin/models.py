from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        return super(Category, self).save(*args, **kwargs)


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.description = self.description.capitalize()
        return super(Book, self).save(*args, **kwargs)


class Issued_Book(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.CharField(max_length=70)
    email = models.EmailField()
    address = models.TextField()
    issued_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    charge_per_day = models.PositiveIntegerField()
    total_charge = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.username = self.username.title()
        if self.return_date != None:
            days = self.return_date - self.issued_date
            self.total_charge = days.days * self.charge_per_day
        return super(Issued_Book, self).save(*args, **kwargs)