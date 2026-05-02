from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, DashboardView, AdminStatsView

router = DefaultRouter()
router.register(r'', ProjectViewSet, basename='project')

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('admin-stats/', AdminStatsView.as_view(), name='admin_stats'),
    path('', include(router.urls)),
]
