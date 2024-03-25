from rest_framework import serializers
from todoapp.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'body', 'created', 'completed']

# class TodoToggleCompleteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ['id']
#         read_only_fields = ['title', 'body', 'created', 'completed']