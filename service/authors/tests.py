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
# from mixer.backend.django import mixer
from django.contrib.auth.models import User
from authors.views import AuthorViewSet
from authors.models import Author,Book


class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorViewSet.as_view({'get':'list'})
        response = view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_create_guest(self):
        """Тест на создания автора анонимным пользователем"""
        factory = APIRequestFactory()
        request = factory.post('/api/authors/',
                               {'name':'Пушкин','birthday_year':1799} ,
                               format='json')
        view = AuthorViewSet.as_view({'get': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_author_for_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/',
                               {'name': 'Пушкин', 'birthday_year': 1799},
                               format='json')
        admin = User.objects.create_superuser('maximy','mksadmin@gmail.com','sync')
        force_authenticate(request,admin)
        view = AuthorViewSet.as_view({'get': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)