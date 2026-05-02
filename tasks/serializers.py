from rest_framework import serializers
from .models import Task, TaskImage
from accounts.serializers import UserSerializer
from projects.serializers import ProjectSerializer

class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('id', 'image', 'uploaded_at')

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_detail = UserSerializer(source='assigned_to', read_only=True)
    project_detail = ProjectSerializer(source='project', read_only=True)
    images = TaskImageSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = (
            'id', 'title', 'description', 'project', 'project_detail',
            'assigned_to', 'assigned_to_detail', 'status', 'priority',
            'due_date', 'created_at', 'updated_at',
            'submission_code', 'submission_design', 'submission_docs',
            'submission_reports', 'submission_date', 'rating', 'images'
        )

