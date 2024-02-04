from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    # 1 masala kitoblari hammasini olish
    all_books = Book.objects.all()

    # 2 masala
    alls = Book.objects.all()
 
    # 3 masala barcha authoours olish
    all_authours = Author.objects.all()

    # 4 masala
    all = Author.objects.all()


    # 5 masala barcha janrlar
    all_genre = Genre.objects.all()

    # 6 masala nashriyotlar royhati
    all_publisher = Publisher.objects.all()
    context = {
        #1 masala 
        'all_books' : all_books,
        
        #2 masala
        'alls' : alls, 

        #3 masala
        'all_authours' : all_authours,
        
        #4 masala
        'all' : all, 


        #5 masala
        'all_genre' : all_genre,

        #6 masala
        'all_publisher' : all_publisher,

    }
    return render ( request,'index.html', context)




