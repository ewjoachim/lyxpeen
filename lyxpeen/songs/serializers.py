from rest_framework import serializers
from . import models


class FolderSerializer(serializers.ModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song-detail'
    )

    class Meta:
        model = models.Folder
        fields = ["id", "name", "description", "priority", "songs"]


class SongSerializer(serializers.ModelSerializer):
    song_parts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='songpart-detail'
    )
    files = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='songfile-detail'
    )

    class Meta:
        model = models.Song
        fields = ["id", "folder", "name", "xml_file", "score_file", "song_parts", "files"]


class SongPartSerializer(serializers.ModelSerializer):
    singer_parts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='singerpart-detail'
    )
    class Meta:
        model = models.SongPart
        fields = ["id", "name", "section", "song", "singer_parts"]


class SectionSerializer(serializers.ModelSerializer):
    song_parts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='songpart-detail'
    )
    singers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='singer-detail'
    )
    class Meta:
        model = models.Section
        fields = ["id", "name", "color", "song_parts", "singers"]


class SingerPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SingerPart
        fields = ["id", "main", "song_part", "singer"]


class SingerSerializer(serializers.ModelSerializer):
    singer_parts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='singerpart-detail'
    )
    class Meta:
        model = models.Singer
        fields = ["id", "user", "main_section", "active", "singer_parts"]


class SongFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SongFile
        fields = ["id", "active", "path", "song", "is_xml", "is_score"]
