
from django.contrib import admin
from django.urls import path, include
from Home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    path('acco/', include('accounts.urls')),

    path('app/', include('app.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
