from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer

def book_list(request):
    books = Book.objects.all()
    bookserializer = BookSerializer(books, many=True)
    return JsonResponse({'drinks':bookserializer.data})