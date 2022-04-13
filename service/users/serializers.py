from rest_framework.serializers import ModelSerializer,StringRelatedField
from rest_framework import serializers
from .models import User,Project,ToDo_list
from .models import User as User_test
from django.contrib.auth.models import User

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User_test
        fields = ('username','email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class UserAdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ToDolistModelSerializer(ModelSerializer):

    class Meta:
        model = ToDo_list
        fields = ['project_name','text','user']
