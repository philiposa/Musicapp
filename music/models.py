from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Album(BaseModel):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(BaseModel):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_songs')
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    youtube_link = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.song_title


class Podcast(BaseModel):
    podcast_title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    podcast_logo = models.CharField(max_length=30)
