from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app01.models import Book
from app01.ser import BookSerializer
from rest_framework.response import Response
from app01.utils import MyResponse


class BookView(APIView):
    def get(self, request, pk):
        book = Book.objects.filter(pk=pk).first()
        book_ser = BookSerializer(book)
        return Response(book_ser.data)

    def put(self, request, pk):
        response_msg = {'status': 100, 'msg': '成功'}
        book = Book.objects.filter(id=pk).first()
        book_ser = BookSerializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            response_msg['data'] = book_ser.data
        else:
            response_msg['status'] = 101
            response_msg['msg'] = '数据校验失败'
            response_msg['data'] = book_ser.errors
        return Response(response_msg)

    def delete(self, request, pk):
        response_msg = MyResponse()
        book = Book.objects.filter(pk=pk).first()
        book_ser = BookSerializer(book)
        book.delete()
        response_msg.data = book_ser.data
        return Response(response_msg.get_dict)


class BooksView(APIView):
    # def get(self, request):
    #     response_msg = {'status': 100, 'msg': '成功'}
    #     books = Book.objects.all()
    #     books_ser = BookSerializer(books, many=True)
    #     response_msg['data'] = books_ser.data
    #     return Response(response_msg)
    def get(self, request):
        response = MyResponse()
        books = Book.objects.all()
        books_ser = BookSerializer(books, many=True)
        response.data = books_ser.data
        return Response(response.get_dict)

    def post(self, request):
        response_msg = {'status': 100, 'msg': '成功'}
        book_ser = BookSerializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            response_msg['data'] = book_ser.data
        else:
            response_msg['status'] = '101'
            response_msg['msg'] = '数据校验失败'
            response_msg['data'] = book_ser.errors
        return Response(response_msg)
