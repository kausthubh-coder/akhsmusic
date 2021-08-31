from django.db import models

# Create your models here.
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    song = models.FileField(upload_to='media')

    def __str__(self):
        return self.name