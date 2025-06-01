from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),  # This makes it the default/home route
    path('upload/', views.upload_file, name='upload_file'),
    path('success/', views.upload_success, name='upload_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

