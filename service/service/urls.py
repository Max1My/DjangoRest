from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
