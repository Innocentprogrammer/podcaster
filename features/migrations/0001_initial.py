# Generated by Django 5.0.2 on 2025-04-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('thumbnil', models.ImageField(upload_to='thumbnails/')),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('mostpopular', 'Most Popular'), ('comedy', 'Comedy'), ('news', 'News'), ('crime', 'Crime'), ('sports', 'Sports')], default='-1', max_length=50)),
                ('video', models.FileField(upload_to='podcasts/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
