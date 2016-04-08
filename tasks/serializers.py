from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'state', 'publish_date', 'user')


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks', 'user')