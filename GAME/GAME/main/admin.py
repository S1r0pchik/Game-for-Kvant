from django.contrib import admin
from .models import Team, Hint, Position_of_Game

def turn_on(modeladmin, request, queryset):
    queryset.update(position='1')

def turn_off(modeladmin, request, queryset):
    queryset.update(position='0')

class Position_of_GameAdmin(admin.ModelAdmin):
    actions = [turn_on, turn_off]

admin.site.register(Team),
admin.site.register(Hint),
admin.site.register(Position_of_Game, Position_of_GameAdmin)