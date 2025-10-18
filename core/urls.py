
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
def ping(request):
    return JsonResponse({"status": "ok"})
urlpatterns = [
    path('ping/',ping),
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/recipes/', include('recipes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
