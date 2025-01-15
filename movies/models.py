from django.db import models
from .upload_files_github import GitHubStorage


class Kinolar(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='kino/', max_length=600, storage=GitHubStorage())
    video_fayl = models.FileField(upload_to='kino/', max_length=600, storage=GitHubStorage())
    genre = models.CharField(max_length=255)
    sight_age = models.CharField(max_length=20)
    reyting = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Multfilm(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='multfilm/', max_length=600, storage=GitHubStorage())
    video_fayl = models.FileField(upload_to='multfilm/', max_length=600, storage=GitHubStorage())
    sight_age = models.CharField(max_length=20)
    genre = models.CharField(max_length=255)
    reyting = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Serial(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='serial/', max_length=600, storage=GitHubStorage())
    video_fayl = models.FileField(upload_to='serial/', max_length=600, storage=GitHubStorage())
    sight_age = models.CharField(max_length=20)
    genre = models.CharField(max_length=255)
    reyting = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Serial_item(models.Model):
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    part = models.IntegerField()
    img = models.ImageField(upload_to='serial_item/', max_length=600, storage=GitHubStorage())
    video_fayl = models.FileField(upload_to='serial_item/', max_length=600, storage=GitHubStorage())
    description = models.TextField()

    def __str__(self):
        return self.name


class Anime(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='anime/', max_length=600, storage=GitHubStorage())
    video_fayl = models.FileField(upload_to='anime/', max_length=600, storage=GitHubStorage())
    genre = models.CharField(max_length=255)
    sight_age = models.CharField(max_length=20)
    reyting = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Anime_item(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    part = models.IntegerField()
    img = models.ImageField(upload_to='anime_item/', max_length=600, storage=GitHubStorage())
    video_fayl = models.FileField(upload_to='anime_item/', max_length=600, storage=GitHubStorage())
    description = models.TextField()

    def __str__(self):
        return self.name
