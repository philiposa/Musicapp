from music import views
from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('podcast/', views.get),
    path('podcast/add/', views.add)
]

urlpatterns = format_suffix_patterns(urlpatterns)
