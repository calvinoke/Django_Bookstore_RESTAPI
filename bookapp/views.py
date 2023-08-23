#from django.shortcuts import render
#from rest_framework.response import Response
#from . models import Book
#from rest_framework.decorators import api_view
#from . serializers import BookSerializer
#from rest_framework import status

# Create your views here.
#Getting all resource objects from the database
#@api_view(['GET'])
#def book_list(request):
 #   books = Book.objects.all()  #Complex data
 #   serializer = BookSerializer(books, many=True)
 #   return Response(serializer.data)


#Posting data into the database
#@api_view(['POST'])
#def book_create(request):
 #   serializer = BookSerializer(data = request.data)
  #  if serializer.is_valid():
  #      serializer.save()
   #     return Response(serializer.data)
   # else:
   #     Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#@api_view(['GET','PUT','DELETE'])
#def book(request,pk):
 #   try:
 #       book = Book.objects.get(pk=pk)#complex data
 #   except:
 #       return Response({'error': 'Book not found'},status = status.HTTP_404_NOT_FOUND)

    #getting the individual book details
  #  if request.method == "GET":
  #      serializer = BookSerializer(book)
 #       return Response(serializer.data)

    #updating the book record or information
    #if request.method == "PUT":
        # book = Book.objects.get(pk=pk)#complex data
      #   serializer = BookSerializer(book, data=request.data)
      #   if serializer.is_valid():
      #      serializer.save()
       #     return Response(serializer.data)
       #  return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #deleting the book record or information
    #if request.method == "DELETE":
    #    book.delete()
     #   return Response(status = status.HTTP_204_NO_CONTENT)

##class Based view
from rest_framework.views import APIView
from . models import Book
from . serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()# complex data from the model
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk = pk)
        except:
            return Response({'error': 'Book does not exist!!'}, status = status.HTTP_404_NOT_FOUND)

    def get(self, request,pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)





