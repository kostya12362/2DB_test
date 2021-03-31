from django.contrib import admin
from django.urls import path, include
from task_api.yasg import urlpatterns as doc_urls
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/messages/', include('api_messages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += doc_urls
