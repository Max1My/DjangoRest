from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'

class BookSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
