from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app01.models import Book
from app01.ser import BookSerializer
from rest_framework.response import Response


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
