from django.urls import path
from .views import AuthorViewSet

app_name = 'author_app'
urlpatterns = [
    path('',AuthorViewSet.as_view())
]