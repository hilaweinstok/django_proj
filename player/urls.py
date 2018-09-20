from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from .views import home

# URL that will match everything ending with 'home', this is why it doesnt have ^
urlpatterns = [
    url(r'home$', home, name="player_home"),
    url(r'login$', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    url(r'logout$', LogoutView.as_view(), name="player_logout")
]
