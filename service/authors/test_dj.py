import json
from pprint import pprint

from django.test import TestCase
from rest_framework import status
from rest_framework.test import (
    APIRequestFactory,
    force_authenticate,
    APIClient,
    APISimpleTestCase,
    APITestCase
)
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from authors.views import AuthorViewSet
from authors.models import Author, Book


class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        """Тест на создания автора анонимным пользователем"""
        factory = APIRequestFactory()
        request = factory.post('/api/authors/',
                               {'name': 'Пушкин', 'birthday_year': 1799},
                               format='json')
        view = AuthorViewSet.as_view({'get': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_author_for_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/',
                               {'name': 'Пушкин', 'birthday_year': 1799},
                               format='json')
        admin = User.objects.create_superuser('maximy', 'mksadmin@gmail.com', 'sync')
        force_authenticate(request, admin)
        view = AuthorViewSet.as_view({'get': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_detail(self):
        author = Author.objects.create(name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Author.objects.create(name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.put(f'/api/authors/{author.id}/', {
            'name': 'Грин',
            'birthday_year': 1880
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(name='Пушкин', birthday_year=1799)
        client = APIClient()
        admin = User.objects.create_superuser('maximy', 'mksadmin@gmail.com', 'sync')
        client.login(username='maximy', password='sync')
        response = client.put(f'/api/authors/{author.id}/', {
            'name': 'Грин',
            'birthday_year': 1880
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(id=author.id)
        self.assertEqual(author.name, 'Грин')
        self.assertEqual(author.birthday_year, 1880)
        client.logout()


class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestBookViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        author = Author.objects.create(name='Пушкин', birthday_year=1799)
        book = Book.objects.create(name='Пиковая дама', author=author)
        admin = User.objects.create_superuser('maximy', 'admin@gmail.com', 'sync')
        self.client.login(username='maximy', password='sync')
        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Руслан и Людмила',
                                                              'author': book.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(id=book.id)
        self.assertEqual(book.name, 'Руслан и Людмила')

    def test_edit_mixer(self):
        book = mixer.blend(Book)
        admin = User.objects.create_superuser('maximy', 'admin@gmail.com', 'sync')



        self.client.login(username='maximy', password='sync')
        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Руслан и Людмила',
                                                              'author': book.author.id})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        book = Book.objects.get(id=book.id)
        print(book.id,book.author,book.name)
        self.assertEqual(book.name,'Руслан и Людмила')
