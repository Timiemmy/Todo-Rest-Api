from rest_framework import serializers
from todoapp.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()


    class Meta:
        model = Todo
        fields = ['id', 'title', 'body', 'created', 'completed']