from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class BookSerializer(serializers.Serializer):
    # id = serializers.CharField()
    title = serializers.CharField(max_length=16, min_length=4)
    author = serializers.CharField()
    price = serializers.CharField()
    publisher = serializers.CharField()

    def validate_price(self, data):
        if float(data) > 10:
            return data
        else:
            raise ValidationError('价格太低')

    def validate(self, validate_data):
        author = validate_data.get('author')
        publisher = validate_data.get('publisher')
        if publisher==author:
            raise ValidationError('作者和出版社不能为同一人')
        return validate_data

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.price = validated_data.get('price')
        instance.author = validated_data.get('author')
        instance.publisher = validated_data.get('publisher')
        instance.save()
        return instance
