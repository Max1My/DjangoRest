from rest_framework.serializers import ModelSerializer,StringRelatedField
from rest_framework import serializers
from .models import User,Project,ToDo_list

class UserModelSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64)


    # class Meta:
    #     model = User
    #     fields = ['username']

class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['name','users']

class ToDolistModelSerializer(ModelSerializer):

    class Meta:
        model = ToDo_list
        fields = ['project_name','text','user']

user1 = User('maximy')
serializer = UserModelSerializer(User)
print(serializer.data)  # {'name': 'Грин', 'birthday_year': 1880}

TodoList1 = ToDo_list(1,'DjangoRestFramework','create project', user1)
serializer = ToDolistModelSerializer(TodoList1)
print(serializer.data)

project = Project(1,'DjangoRestFramework', user1)  # {'name': 'Некоторая книга', 'authors': [OrderedDict([('name', 'Грин'), ('birthday_year', 1880)]), OrderedDict([('name', 'Пушкин'), ('birthday_year', 1799)])]}
serializer = ProjectModelSerializer(project)
print(serializer.data)
