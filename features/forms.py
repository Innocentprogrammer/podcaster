from django import forms
from .models import Podcast

class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ['title', 'thumbnail', 'description', 'category', 'video', 'audio']  # added 'audio'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'audio': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'audio/*'
            }),  # new widget for optional audio
        }
        
    def clean(self):
        cleaned_data = super().clean()

        video = cleaned_data.get('video')
        audio = cleaned_data.get('audio')

        # If both video and audio are empty, raise a validation error
        if not video and not audio:
            raise forms.ValidationError('You must upload either a video or an audio file.')

        # If both video and audio are filled, raise a validation error
        if video and audio:
            raise forms.ValidationError('Please upload either a video or an audio file, not both.')

        return cleaned_data