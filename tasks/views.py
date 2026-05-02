from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from core.permissions import IsAdminUser, IsProjectOwnerOrMember

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['project', 'status', 'priority', 'assigned_to']
    search_fields = ['title', 'description']

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [IsAdminUser()]
        return [permissions.IsAuthenticated(), IsProjectOwnerOrMember()]

    def get_queryset(self):
        user = self.request.user
        isAdmin = user.email.endswith('@task.com') or user.role == 'Admin'
        if isAdmin:
            return Task.objects.select_related('assigned_to', 'project', 'project__owner').prefetch_related('images', 'project__members').all()
        return Task.objects.select_related('assigned_to', 'project', 'project__owner').prefetch_related('images', 'project__members').filter(assigned_to=user)

    def update(self, request, *args, **kwargs):
        user = request.user
        isAdmin = user.email.endswith('@task.com') or user.role == 'Admin'
        if not isAdmin:
            task = self.get_object()
            if task.assigned_to != user:
                return Response({"detail": "You can only update tasks assigned to you."}, status=403)
            
            allowed_fields = ['status', 'submission_code', 'submission_design', 'submission_docs', 'submission_reports', 'submission_date', 'design_images']
            for field in request.data:
                if field not in allowed_fields:
                    return Response({"detail": f"You cannot update field: {field}"}, status=403)

        response = super().update(request, *args, **kwargs)
        
        if response.status_code == 200:
            task = self.get_object()
            images = request.FILES.getlist('design_images')
            if images:
                from .models import TaskImage
                for img in images:
                    TaskImage.objects.create(task=task, image=img)
        
        return response

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def rate(self, request, pk=None):
        task = self.get_object()
        rating = request.data.get('rating')
        if not rating or not (1 <= int(rating) <= 5):
            return Response({"detail": "Valid rating (1-5) required."}, status=400)
        
        task.rating = rating
        task.save()
        return Response({"status": "rating saved"})
