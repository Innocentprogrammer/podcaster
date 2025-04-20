from django.db import models

CATEGORY_CHOICES = [
    ('Most Popular', 'mostpopular'),
    ('Comedy', 'comedy'),
    ('News', 'news'),
    ('Crime', 'crime'),
    ('Sports', 'sports'),
    ('Study', 'study'),
]

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='-1')
    video = models.FileField(upload_to='podcasts/', blank=True, null=True)  # Video is optional
    audio = models.FileField(upload_to='audios/', blank=True, null=True)  # New field for optional audio
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
