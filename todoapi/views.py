from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import TodoSerializer
from todoapp.models import Todo
from .pagination import PagePagination

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
    permission_classes = [IsAuthenticated]
    pagination_class = PagePagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'body']
    ordering_fields = ['title']

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)  # Set user before saving
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.completed = not instance.completed  # Toggle completed value
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


'''
class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.instance.completed = not(serializer.instance.completed)
        serializer.save()
'''
