from restframework import routers
from . import views

router = routers.SimpleRouter()

router.register(r"folders", views.FolderViewSet)
router.register(r"songs", views.SongViewSet)
router.register(r"sections", views.SectionViewSet)
router.register(r"parts", views.PartViewSet)
router.register(r"singers", views.SingerViewSet)
router.register(r"songfiles", views.SongFileViewSet)

urlpatterns = router.urls
