from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkBoard, Task
from .serializers import WorkBoardSerializer, TaskSerializer

def index(request):
    """
    View to render the index page.
    """
    return render(request, 'index.html')

class WorkBoardViewSet(viewsets.ModelViewSet):
    queryset = WorkBoard.objects.all()
    serializer_class = WorkBoardSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
