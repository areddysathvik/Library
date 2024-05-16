from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone 

class CustomUser(AbstractUser):
    borrowed_books = models.ManyToManyField('BookBorrowed', blank=True)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.username

class BookBorrowed(models.Model):
    book_ID = models.IntegerField()
    book_name = models.CharField(max_length=255)
    date_borrowed = models.DateField(default=timezone.now)
    late_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.book_name
