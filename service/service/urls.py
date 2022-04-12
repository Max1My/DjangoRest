from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view
# from authors.views import AuthorModelViewSet,BiographyModelViewSet,BookModelViewSet,ArticleModelViewSet
from users.views import UserModelViewSet,ProjectModelViewSet,TodoListModelViewSet

router = DefaultRouter()
# router.register('authors', AuthorModelViewSet)
# router.register('biographies',BiographyModelViewSet)
# router.register('books', BookModelViewSet)
# router.register('articles', ArticleModelViewSet)
# router.register('users', UserModelViewSet)
router.register('users',UserModelViewSet)
router.register('projects',ProjectModelViewSet)
router.register('todolists',TodoListModelViewSet)

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('schema/',schema_view)
]
