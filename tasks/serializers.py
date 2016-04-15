from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


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


class TokenSerializer(serializers.Serializer):
    pass