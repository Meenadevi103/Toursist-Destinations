from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=200)
    weather = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    google_map_link = models.URLField(blank=True,null=True)
    image = models.ImageField(upload_to='dest_images/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place_name
