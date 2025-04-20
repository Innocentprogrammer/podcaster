from django.contrib import admin
from .models import Podcast

class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail', 'description', 'category', 'video', 'audio', 'uploaded_at']

admin.site.register(Podcast,PodcastAdmin)


