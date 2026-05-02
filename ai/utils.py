from google import genai
import os
from django.conf import settings

def get_gemini_response(prompt):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return "Gemini API key not configured."
    
    client = genai.Client(api_key=api_key)
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite',
            contents=prompt
        )
        return response.text
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower():
            return "AI service is currently at capacity (Quota Exceeded). Please try again in a few minutes."
        return f"AI Error: {error_msg}"

def generate_subtasks(task_description):
    prompt = f"Break down the following task into 3-5 actionable subtasks. Format as a bulleted list: {task_description}"
    return get_gemini_response(prompt)

def suggest_priority(task_title, task_description):
    prompt = f"Based on the following task title and description, suggest a priority (Low, Medium, or High) and give a brief reason. Title: {task_title}, Description: {task_description}"
    return get_gemini_response(prompt)

def summarize_progress(tasks_data):
    prompt = f"Summarize the following project progress based on these tasks: {tasks_data}. Provide a concise daily summary."
    return get_gemini_response(prompt)
