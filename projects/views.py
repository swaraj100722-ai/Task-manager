from rest_framework import viewsets, permissions, views
from rest_framework.response import Response
from django.utils import timezone
from .models import Project
from tasks.models import Task
from .serializers import ProjectSerializer
from core.permissions import IsAdminUser, IsProjectOwnerOrMember

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['owner', 'members']
    search_fields = ['name', 'description']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [permissions.IsAuthenticated(), IsProjectOwnerOrMember()]

    def get_queryset(self):
        user = self.request.user
        isAdmin = user.email.endswith('@task.com') or user.role == 'Admin'
        if isAdmin:
            return Project.objects.select_related('owner').prefetch_related('members').all()
        from django.db.models import Q
        return Project.objects.select_related('owner').prefetch_related('members').filter(Q(members=user) | Q(owner=user)).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        isAdmin = user.email.endswith('@task.com') or user.role == 'Admin'
        
        if isAdmin:
            projects = Project.objects.all()
            tasks = Task.objects.all()
        else:
            projects = Project.objects.filter(members=user) | Project.objects.filter(owner=user)
            tasks = Task.objects.filter(assigned_to=user)
        
        projects = projects.distinct()
        tasks = tasks.distinct()
        
        total_projects = projects.count()
        total_tasks = tasks.count()
        completed_tasks = tasks.filter(status='Done').count()
        pending_tasks = tasks.exclude(status='Done').count()
        overdue_tasks = tasks.filter(due_date__lt=timezone.now()).exclude(status='Done').count()

        return Response({
            "total_projects": total_projects,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "overdue_tasks": overdue_tasks
        })

class AdminStatsView(views.APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_projects = Project.objects.count()
        total_tasks = Task.objects.count()
        completed_tasks = Task.objects.filter(status='Done').count()
        pending_tasks = Task.objects.exclude(status='Done').count()
        overdue_tasks = Task.objects.filter(due_date__lt=timezone.now()).exclude(status='Done').count()
        
        # Performance calculation (simplified)
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        # Recent tasks - Optimized with select_related/prefetch_related to reduce database hits
        recent_tasks = Task.objects.select_related(
            'assigned_to', 
            'project', 
            'project__owner'
        ).prefetch_related(
            'images', 
            'project__members'
        ).order_by('-created_at')[:5]
        from tasks.serializers import TaskSerializer
        recent_tasks_data = TaskSerializer(recent_tasks, many=True).data

        # Recent projects - Optimized with select_related/prefetch_related
        recent_projects = Project.objects.select_related('owner').prefetch_related('members').order_by('-created_at')[:5]
        recent_projects_data = ProjectSerializer(recent_projects, many=True).data

        return Response({
            "stats": {
                "total_projects": total_projects,
                "total_tasks": total_tasks,
                "completed_tasks": completed_tasks,
                "pending_tasks": pending_tasks,
                "overdue_tasks": overdue_tasks,
                "completion_rate": completion_rate
            },
            "recent_tasks": recent_tasks_data,
            "recent_projects": recent_projects_data
        })
