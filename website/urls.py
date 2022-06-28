from music import views
from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('podcast/', views.PodcastList.as_view()),
    path('episode/', views.EpisodeList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
