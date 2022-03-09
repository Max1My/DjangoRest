from rest_framework.viewsets import ModelViewSet
from .models import User,Project,ToDo_list
from .serializers import UserModelSerializer,ProjectModelSerializer,ToDolistModelSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

class TodoListModelViewSet(ModelViewSet):
    queryset = ToDo_list.objects.all()
    serializer_class = ToDolistModelSerializer