from django.db import models
from django.conf import settings

from lyxpeen.project.helpers import UUIDPkMixin

COLORS = [
    ("aqua", "#7fdbff"),
    ("black", "#111111"),
    ("blue", "#0074d9"),
    ("fuchsia", "#f012be"),
    ("gray", "#aaaaaa"),
    ("green", "#2ecc40"),
    ("lime", "#01ff70"),
    ("maroon", "#85144b"),
    ("navy", "#001f3f"),
    ("olive", "#3d9970"),
    ("orange", "#ff851b"),
    ("purple", "#b10dc9"),
    ("red", "#ff4136"),
    ("silver", "#dddddd"),
    ("teal", "#39cccc"),
    ("yellow", "#ffdc00"),
    ('white', "#ffffff"),
]


class Folder(UUIDPkMixin, models.Model):
    """
    Songs are in folders. Folders are sorted by decreasing priority,
    the top priority folder is the default one.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = "songs"


class Song(UUIDPkMixin, models.Model):
    """
    Songs (may) have an xml file that will be used for generation features.
    """
    folder = models.ForeignKey(Folder, related_name="songs", on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    xml_file = models.ForeignKey("SongFile", null=True, related_name="+")
    score_file = models.ForeignKey("SongFile", null=True, related_name="+")

    def __str__(self):
        return self.name

    class Meta:
        app_label = "songs"


class SongPart(UUIDPkMixin, models.Model):
    """
    Songs have parts (tenor, alto, voice 2, tenor solo, ...)
    """
    name = models.CharField(max_length=100, blank=True)
    song = models.ForeignKey(Song, related_name="song_parts")
    section = models.ForeignKey("Section", related_name="song_parts", null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.song.name, self.name)

class Section(UUIDPkMixin, models.Model):
    """
    The choir has sections (bass, soprano, ...)
    """
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6, choices=[(color, color) for color in COLORS])

    def __str__(self):
        return self.name

    class Meta:
        app_label = "songs"


class SingerPart(UUIDPkMixin, models.Model):
    """
    A given singer can sing a given song part
    """
    is_main_part = models.BooleanField(default=True)
    song_part = models.ForeignKey(SongPart, related_name="singer_parts")
    singer = models.ForeignKey("Singer", related_name="singer_parts")

    class Meta:
        app_label = "songs"


class Singer(UUIDPkMixin, models.Model):
    """
    Singers can be linked to site users.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    main_section = models.ForeignKey(Section, related_name='singers', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = "songs"



class SongFile(UUIDPkMixin, models.Model):
    """
    Files are linked to songs. xml files can be used for generation features.
    """
    path = models.FileField()

    song = models.ForeignKey(Song, related_name='files')

    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_xml = models.BooleanField(default=False)
    is_score = models.BooleanField(default=False)

    def __str__(self):
        return self.path.path

    class Meta:
        app_label = "songs"
