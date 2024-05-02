from django.shortcuts import render
from django.shortcuts import render
from app.search_model.utils.search_model.api_google_books import search_books
from app.search_model.models.book_model import *

def search_books_view(request):

    query = Book.objects.all()

    query = request.GET.get('query','')
    if query:
        books_data = search_books(query)

        # for item in books_data:
        #     # Use get_or_create to avoid creating duplicate entries
        #     livro, created = Book.objects.get_or_create(titulo=item['title'])

        #     if created:
        #         print(f"Criado um novo registro para o livro: {item['title']}")
        #     else:
        #         print(f"O livro: {item['title']} já existe no banco de dados.")

        return render(request, 'books/pages/search_results.html', {'books': books_data})
    else:
        return render(request, 'books/pages/search_form.html')

def library_view(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'books/pages/digital_library.html', {'books':books})
