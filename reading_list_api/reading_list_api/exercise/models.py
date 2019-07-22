from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    uid = models.UUIDField()
    cover = models.URLField()
    isbn = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.ForeignKey('exercise.Author', on_delete=models.CASCADE)
    published = models.DateTimeField()
    publisher = models.ForeignKey('exercise.Publisher', on_delete=models.SET_NULL, null=True)
    pages = models.IntegerField(null=True)
    description = models.TextField(blank=True, default="")
    website = models.URLField(blank=True, default="")

    def __str__(self):
        return f"{self.title} ({self.author.name})"
