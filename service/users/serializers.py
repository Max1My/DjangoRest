from rest_framework.serializers import ModelSerializer,StringRelatedField
from rest_framework import serializers
from .models import User,Project,ToDo_list

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['name','users']

class ToDolistModelSerializer(ModelSerializer):

    class Meta:
        model = ToDo_list
        fields = ['project_name','text','user']
