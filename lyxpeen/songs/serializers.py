from rest_framework import serializers
from . import models


class FolderSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Folder
        fields = ["id", "name", "description", "priority", "songs"]


class SongPartSerializer(serializers.ModelSerializer):
    singer_parts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = models.SongPart
        fields = ["id", "name", "section", "song", "singer_parts"]


class SongSerializer(serializers.ModelSerializer):
    song_parts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    files = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Song
        fields = ["id", "folder", "name", "song_parts", "files"]


class SectionSerializer(serializers.ModelSerializer):
    song_parts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    singers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Section
        fields = ["id", "name", "color", "song_parts", "singers"]


class SingerPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SingerPart
        fields = ["id", "is_main_part", "song_part", "singer"]


class SingerSerializer(serializers.ModelSerializer):
    singer_parts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Singer
        fields = ["id", "user", "main_section", "is_active", "singer_parts"]


class SongFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SongFile
        fields = ["id", "is_active", "path", "song", "is_main_file", "is_xml", "is_score"]
