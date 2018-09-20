from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE, Q

GAME_STATUS = (
    ('F', 'First player move'),
    ('S', 'Second player move'),
    ('F', 'Game has finished')
)


class GameQuerySet(models.QuerySet):
    def games_for_user(self, user):
        return self.filter(Q(first_player=user) | Q(second_player=user))

    def active(self):
        """ This is returning only the active games """
        return self.filter(Q(status='F') | Q(status='S'))


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=CASCADE)
    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS)
    # returns a manager object that includes the function form the custom query set overriding the objects attr
    objects = GameQuerySet.as_manager()

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True)
    by_first_player = models.BooleanField()
    game = models.ForeignKey(Game, on_delete=CASCADE)
