from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    website = models.URLField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)