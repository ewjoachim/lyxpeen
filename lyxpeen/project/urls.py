from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from lyxpeen.songs import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = routers.SimpleRouter()

router.register(r"folders", views.FolderViewSet)
router.register(r"songs", views.SongViewSet)
router.register(r"sections", views.SectionViewSet)
router.register(r"song_parts", views.SongPartViewSet)
router.register(r"singer_parts", views.SingerPartViewSet)
router.register(r"singers", views.SingerViewSet)
router.register(r"song_files", views.SongFileViewSet)

urlpatterns += router.urls
