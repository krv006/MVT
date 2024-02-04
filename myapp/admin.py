from django.contrib import admin
from .models import Genre, Author, Publisher, Book
# Register your models here.



@admin.register(Genre)
class Genre(admin.ModelAdmin):
    list_display = ('name', "id")


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('name', "id", 'birth_date', 'nationality')



@admin.register(Publisher)
class Publisher(admin.ModelAdmin):
    list_display = ['name','id','website']




@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ['title', "id",'publication_date', 'price',]