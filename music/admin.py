from django.contrib import admin
from .models import Album, Song, Podcast, Episode

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(Episode)