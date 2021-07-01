from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()


class Review(models.Model):
    text = models.TextField()
    score = models.IntegerField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='titles')
    category = models.ManyToManyField(Category, related_name='titles')
