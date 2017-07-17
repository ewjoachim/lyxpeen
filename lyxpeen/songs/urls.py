from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r"folders", views.FolderViewSet)
router.register(r"songs", views.SongViewSet)
router.register(r"sections", views.SectionViewSet)
router.register(r"song_parts", views.SongPartViewSet)
router.register(r"singer_parts", views.SingerPartViewSet)
router.register(r"singers", views.SingerViewSet)
router.register(r"song_files", views.SongFileViewSet)

urlpatterns = router.urls
