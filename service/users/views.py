from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.views import Response
from rest_framework import status,permissions
from .models import User,Project,ToDo_list
from .serializers import UserModelSerializer,ProjectModelSerializer,ToDolistModelSerializer





class UserModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer



class ProjectModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        headers['bababa'] = ''
        return Response(serializer.data,status=status.HTTP_201_CREATED,headers=headers)


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
