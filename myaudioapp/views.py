from django.shortcuts import render
from myaudioapp.models import MyAudio,Song,Podcast,Audiobook
from myaudioapp.serializers import MyAudioSerializer,SongSerializer,PodcastSerializer,AudiobookSerializer
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework import viewsets

# Create your views here.
class MyAudioViewSet(viewsets.ModelViewSet):
    queryset = MyAudio.objects.all()
    serializer_class = MyAudioSerializer 

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer 

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer 

class AudioBookViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer 