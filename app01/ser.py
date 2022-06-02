from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    author = serializers.CharField()
    price = serializers.CharField()
    publisher = serializers.CharField()
