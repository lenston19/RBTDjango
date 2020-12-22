from django.db import models

# Create your models here.

album_list = (
    [1, '58'],
    [2, 'Что они знают?'],
    [3, 'Холостяк']
)

class PlaylistTrack(models.Model):
    TrackImg = models.ImageField(null=False, blank=True, verbose_name='Обложка')
    TrackName = models.CharField(max_length=100, verbose_name='Название трека')
    TrackAuthor = models.CharField(max_length=250, verbose_name='Авторы трека')
    TrackTime = models.CharField(max_length=250, verbose_name='Время трека')

    class Meta:
        db_table = "Чарт"
        verbose_name = 'Трэк'
        verbose_name_plural = 'Чарт'

    def __str__(self):
        return f"{self.TrackName}"

class PlaylistEgorCrid(models.Model):
    TrackImg = models.ImageField(null=False, blank=True, verbose_name='Обложка')
    TrackAlbum = models.IntegerField(choices=album_list, verbose_name='Альбом')
    TrackName = models.CharField(max_length=100, verbose_name='Название трека')
    TrackAuthor = models.CharField(max_length=250, verbose_name='Авторы трека', default='Егор Крид')
    TrackTime = models.CharField(max_length=250, verbose_name='Время трека')

    class Meta:
        db_table = "Егор Крид"
        verbose_name = 'Трэк'
        verbose_name_plural = 'Егор Крид'

    def __str__(self):
        return f"{self.TrackName}"