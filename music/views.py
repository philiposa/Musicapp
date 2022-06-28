from django.http import Http404
from django.shortcuts import render
from .models import Album, Podcast, Episode
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PodcastSerializer, EpisodeSerializer


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.filter(pk=album_id).first()
    except Album.DoesNotExist:
        raise Http404('Album does not exist')
    return render(request, 'music/detail.html', {'album': album})


class PodcastList(APIView):
    def get(self, request):
        podcasts = Podcast.objects.all()
        serializers = PodcastSerializer(podcasts, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = PodcastSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)


class EpisodeList(APIView):
    def get(self, request):
        episodes = Episode.objects.all()
        serializers = EpisodeSerializer(episodes, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = EpisodeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
