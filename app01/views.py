from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app01.models import Book
from app01.ser import BookSerializer


class BookView(APIView):
    def get(self, request, pk):
        book = Book.objects.filter(pk=pk).first()
