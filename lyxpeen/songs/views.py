from rest_framework import viewsets, exceptions
from rest_framework.decorators import list_route
from rest_framework.response import Response

from . import serializers
from . import models


class FolderViewSet(viewsets.ModelViewSet):
    queryset = models.Folder.objects.all()
    serializer_class = serializers.FolderSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer

    @list_route(methods=['get'])
    def random(self, request):
        """
        Return a random song from the top priority folder
        """
        # I know it's suboptimal, let's not fix until it becomes a
        # problem and someone has a better solution.
        queryset = self.queryset.filter(
            folder=models.Folder.objects.latest("priority"))
        random_song = queryset.order_by("?").first()
        return Response(self.serializer_class(random_song).data)


class SectionViewSet(viewsets.ModelViewSet):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer


class SongPartViewSet(viewsets.ModelViewSet):
    queryset = models.SongPart.objects.all()
    serializer_class = serializers.SongPartSerializer


class SingerPartViewSet(viewsets.ModelViewSet):
    queryset = models.SingerPart.objects.all()
    serializer_class = serializers.SingerPartSerializer


class SingerViewSet(viewsets.ModelViewSet):
    queryset = models.Singer.objects.all()
    serializer_class = serializers.SingerSerializer


class SongFileViewSet(viewsets.ModelViewSet):
    queryset = models.SongFile.objects.all()
    serializer_class = serializers.SongFileSerializer

    def perform_create(self, serializer):
        from django.contrib.auth.models import User
        serializer.save(uploaded_by=User.objects.get(username="joachim"))
