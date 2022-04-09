import json
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
from service.authors.views import AuthorViewSet
from service.authors.models import Author,Book


class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorViewSet.as_view({'get':'list'})
        response = view(request)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)