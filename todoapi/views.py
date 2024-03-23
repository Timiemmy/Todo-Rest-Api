from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import TodoSerializer
from todoapp.models import Todo

"""
class TodoListView(generics.ListAPIView):
    # ListApiView requires two mandatory attributes: serializer_class and queryset.
    serializer_class = TodoSerializer
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')
"""


class TodoListCreateView(generics.ListCreateAPIView):
    # ListApiView requires two mandatory attributes: serializer_class and queryset.
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)  # Set user before saving
        return Response(serializer.data, status=status.HTTP_201_CREATED)
