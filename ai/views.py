from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import generate_subtasks, suggest_priority, summarize_progress

class AIGenerateTasksView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        description = request.data.get('description')
        if not description:
            return Response({"error": "Description is required"}, status=400)
        
        subtasks = generate_subtasks(description)
        return Response({"subtasks": subtasks})

class AIPrioritySuggestionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        if not title:
            return Response({"error": "Title is required"}, status=400)
        
        suggestion = suggest_priority(title, description)
        return Response({"suggestion": suggestion})

class AISummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tasks = request.data.get('tasks')
        if not tasks:
            return Response({"error": "Tasks data is required"}, status=400)
        
        summary = summarize_progress(tasks)
        return Response({"summary": summary})
