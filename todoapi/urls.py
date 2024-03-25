from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListCreateView.as_view()),
    path("<int:pk>/", views.TodoRetrieveUpdateDestroy.as_view()),
    #path("<int:pk>/complete", views.TodoToggleComplete.as_view()),
]