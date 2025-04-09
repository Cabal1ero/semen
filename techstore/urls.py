from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Импортируем представления из текущего пакета

urlpatterns = [
    path('admin/', admin.site.urls),
    # Добавляем URL для django_browser_reload
    path("__reload__/", include("django_browser_reload.urls")),
    # Добавляем маршрут для корневого URL
    path('', views.home, name='home'),  # Этот маршрут будет обрабатывать корневой URL
    path('computers/', views.computers, name='computers'),
    # Добавляем URL для авторизации
    #path('accounts/', include('accounts.urls')),
]

# Добавляем URL для медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
