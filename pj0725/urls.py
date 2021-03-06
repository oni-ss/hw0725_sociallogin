from django.contrib import admin
from django.urls import path, include
from app0725 import views
from app0725 import urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app0725/', include('app0725.urls')),
    path('', views.home, name="home"),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
