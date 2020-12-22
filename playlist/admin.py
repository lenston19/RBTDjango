from django.contrib import admin

from .models import PlaylistTrack, PlaylistEgorCrid

# Register your models here.
@admin.register(PlaylistTrack)
class ChartAdmin(admin.ModelAdmin):
    list_display = ('TrackName','TrackAuthor','TrackTime')
    list_filter = ('TrackAuthor', )

@admin.register(PlaylistEgorCrid)
class EgorCridAdmin(admin.ModelAdmin):
    list_display = ('TrackAlbum', 'TrackName', 'TrackAuthor', 'TrackTime')
    list_filter = ('TrackName','TrackAlbum',)
