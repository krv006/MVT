from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    #1 masala kitoblari hammasini olish
    all_books = Book.objects.all()
    # 3 masala barcha authoours olish
    all_authours = Author.objects.all()

    # 5 masala barcha janrlar
    all_genre = Genre.objects.all()
    context = {
        #1 masala 
        'all_books' : all_books,
        
        #3 masala
        'all_authours' : all_authours,
        
        #5 masala
        'all_genre' : all_genre,

    }
    return render ( request,'index.html', context)




