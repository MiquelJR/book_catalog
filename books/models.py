# books/models.py

from django.db import models

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
