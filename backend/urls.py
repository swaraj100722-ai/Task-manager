from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('index.html', TemplateView.as_view(template_name='index.html')),
    path('landing.html', TemplateView.as_view(template_name='landing.html')),
    
    # Direct mappings for main pages in subfolder
    path('pages/admin.html', TemplateView.as_view(template_name='pages/admin.html')),
    path('pages/projects.html', TemplateView.as_view(template_name='pages/projects.html')),
    path('pages/tasks.html', TemplateView.as_view(template_name='pages/tasks.html')),
    path('pages/ai_helper.html', TemplateView.as_view(template_name='pages/ai_helper.html')),
    path('pages/settings.html', TemplateView.as_view(template_name='pages/settings.html')),
    path('pages/submission_detail.html', TemplateView.as_view(template_name='pages/submission_detail.html')),

    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/ai/', include('ai.urls')),
]

# Serve static and media files always (Whitenoise will handle static in production, 
# but these helpers ensure the URLs are correctly mapped)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static('/pages/', document_root=settings.BASE_DIR / 'frontend' / 'pages')
urlpatterns += static('/css/', document_root=settings.BASE_DIR / 'frontend' / 'css')
urlpatterns += static('/js/', document_root=settings.BASE_DIR / 'frontend' / 'js')
urlpatterns += static('/assets/', document_root=settings.BASE_DIR / 'frontend' / 'assets')
