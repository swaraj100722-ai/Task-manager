from django.db import models
from django.conf import settings
from projects.models import Project

class Task(models.Model):
    STATUS_CHOICES = (
        ('Todo', 'Todo'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    )
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Todo')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Submission fields
    submission_code = models.URLField(max_length=500, null=True, blank=True)
    submission_design = models.URLField(max_length=500, null=True, blank=True)
    submission_docs = models.URLField(max_length=500, null=True, blank=True)
    submission_reports = models.TextField(null=True, blank=True)
    submission_date = models.DateTimeField(null=True, blank=True)
    
    # Admin review
    rating = models.IntegerField(null=True, blank=True, choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.title

class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='task_submissions/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
