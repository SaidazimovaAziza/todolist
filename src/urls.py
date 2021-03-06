from rest_framework.routers import DefaultRouter

from src.views import ToDoViewSet

router = DefaultRouter()

router.register(
    prefix='todo', viewset=ToDoViewSet, basename='todo',
)

urlpatterns = router.urls
