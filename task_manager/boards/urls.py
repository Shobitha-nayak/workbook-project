# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import WorkBoardViewSet, TaskViewSet

# router = DefaultRouter()
# router.register(r'boards', WorkBoardViewSet)
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),      #api/
# ]




from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, WorkBoardViewSet, TaskViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'workboards', WorkBoardViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # URL for the index page
    path('api/', include(router.urls)),  # Include REST API routes
]
