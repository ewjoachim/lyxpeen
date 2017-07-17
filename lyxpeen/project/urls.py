from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework import routers

from lyxpeen.songs.urls import urlpatterns as song_urls
from lyxpeen.users.urls import urlpatterns as user_urls

api_urls = song_urls + user_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls, namespace="api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
