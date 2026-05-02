from django.urls import path
from .views import AIGenerateTasksView, AIPrioritySuggestionView, AISummaryView

urlpatterns = [
    path('generate-tasks/', AIGenerateTasksView.as_view(), name='ai_generate_tasks'),
    path('suggest-priority/', AIPrioritySuggestionView.as_view(), name='ai_suggest_priority'),
    path('summary/', AISummaryView.as_view(), name='ai_summary'),
]
