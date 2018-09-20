from django.contrib import admin
from .models import Game, Move

admin.site.register(Move)


# will make the model show theses fields in the browser
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status',)
