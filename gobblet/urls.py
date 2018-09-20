from django.contrib import admin
from django.conf.urls import url, include

from .views import welcome

# Includes urlpatterns from player/urls.py
# First argument is the url prefix
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^player/', include('player.urls')),
    url(r'^$', welcome, name='gobblet_welcome'),
]
