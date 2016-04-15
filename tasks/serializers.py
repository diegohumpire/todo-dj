from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='task-highlight', format='html')

    class Meta:
        model = Task
        fields = ('url', 'highlight', 'user', 'id', 'title', 'description', 'state', 'publish_date')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks')


class ErrorSerializer(serializers.Serializer):
    error = serializers.BooleanField(default=True)
    message = serializers.CharField(max_length=200)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=40)
    user = UserSerializer()
