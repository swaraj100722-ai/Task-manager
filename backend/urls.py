from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('index.html', TemplateView.as_view(template_name='index.html')),
    path('landing.html', TemplateView.as_view(template_name='landing.html')),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/ai/', include('ai.urls')),
]

if settings.DEBUG:
    # Most specific patterns first
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/pages/', document_root=settings.BASE_DIR / 'frontend' / 'pages')
    urlpatterns += static('/css/', document_root=settings.BASE_DIR / 'frontend' / 'css')
    urlpatterns += static('/js/', document_root=settings.BASE_DIR / 'frontend' / 'js')
    # Broadest pattern last
    urlpatterns += static('/', document_root=settings.BASE_DIR / 'frontend')
