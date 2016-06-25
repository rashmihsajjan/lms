from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    isbn = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    available = models.IntegerField()

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    user_type = models.IntegerField()
    expiry_date = models.DateField()

    def __unicode__(self):
        return self.user.username

class Issue(models.Model):
    book = models.ForeignKey(Book)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='issuedto')
    issued_date = models.DateField()
    due_date = models.DateField()
    issued_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='issuedby')
