from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': 'Welcome to Healthcare Backend API',
        'version': '1.0',
        'endpoints': {
            'authentication': '/api/auth/',
            'patients': '/api/patients/',
            'doctors': '/api/doctors/',
            'mappings': '/api/mappings/',
            'admin': '/admin/',
        },
        'documentation': 'https://github.com/yourusername/healthcare-backend'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/auth/', include('authentication.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/mappings/', include('mappings.urls')),
]