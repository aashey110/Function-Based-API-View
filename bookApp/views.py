from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(pk = pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        book = Book.objects.get(pk = pk)
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            return Response(serializer.data)

    if request.method == "DELETE":
        book = Book.objects.get(pk = pk)
        book.delete()
        return Response({"msg": 'SUCCESSFULLY DELETED'})  