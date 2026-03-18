from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, VisitViewSet, dashboard, UserViewSet

router = DefaultRouter()
router.register('schools', SchoolViewSet)
router.register('visits', VisitViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls + [
    path('dashboard/', dashboard),
]