from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'gallery'

urlpatterns=[
  path('', views.home, name='home'),
  path('search/', views.search_results, name='search'),
] + static(
  settings.MEDIA_URL, 
  document_root = settings.MEDIA_ROOT
)

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)