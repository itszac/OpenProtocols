from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#master class for user content
class Document(models.Model):
    author = models.ForeignKey(User)
    votes = models.IntegerField()
    date_created = models.DateField()

    def __unicode__(self):
        try:
            return self.name
        except:
            return str(self.author.username) + str(self.date_created)

    def vote_up(self):
        self.votes = self.votes + 1
        return self.votes

class Tag(models.Model):
    name = models.CharField(max_length = 100)
    number_protocols = models.IntegerField()

    def __unicode__(self):
        return self.name

class Protocol(Document):
    name = models.CharField(max_length = 225)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    materials = models.ManyToManyField('Material')

    def __unicode__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length = 225)
    description = models.TextField(null = True)

    def __unicode__(self):
        return self.name

class Step(Document):
    protocol = models.ForeignKey(Protocol)
    content = models.TextField()
    order = models.IntegerField()

    def __unicode__(self):
        return self.protocol.name + str(self.order)

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    total_votes = models.IntegerField()
    profile = models.TextField()

    def __unicode__(self):
        return self.user.username

class Comment(Document):
    document = models.ForeignKey(Document, related_name = 'thing_commented_on')
    content = models.TextField()

class Media(models.Model):
    document = models.ForeignKey(Document)
    media_file = models.FileField(upload_to = "/home/zac/python/methods/media")