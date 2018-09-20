from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from play.models import Game


@login_required
def home(request):
    my_game = Game.objects.games_for_user(request.user)
    active_games = my_game.active()

    return render(request, "player/home.html",
                  {'games': active_games})
