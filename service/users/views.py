from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.views import Response
from rest_framework import status
from .models import User,Project,ToDo_list
from .serializers import UserModelSerializer,ProjectModelSerializer,ToDolistModelSerializer



class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filterset_fields = ['username','email']
    pagination_class = UserLimitOffsetPagination

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class ProjectModelViewSet(ViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    filterset_fields = ['name','users']
    pagination_class = ProjectLimitOffsetPagination

    def list(self,request):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoListLimitOffsetPagintaion(LimitOffsetPagination):
    default_limit = 2

class TodoListModelViewSet(ViewSet):
    queryset = ToDo_list.objects.all()
    serializer_class = ToDolistModelSerializer

    def list(self,request):
        todolist = ToDo_list.objects.all()
        serializer = ToDolistModelSerializer(todolist, many=True)
        return Response(serializer.data)

    def get(self, request, format=None):
        todolist = ToDo_list.objects.all()
        serializer = ToDolistModelSerializer(todolist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToDolistModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
