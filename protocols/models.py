from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

#class Ology(models.Model):
#    name = models.CharField(max_length=50)

#    def __unicode__(self):
#        return self.name

#class Category1(models.Model):
#    name = models.CharField(max_length=50)
#    category = models.ManyToManyField(Ology)

#    def __unicode__(self):
#        return self.name

#class Category2(models.Model):
#    name = models.CharField(max_length=50)
#    category = models.ManyToManyField(Category1)

#    def __unicode__(self):
#        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
#    tagtag = models.ForeignKey('self')
#    category = models.ManyToManyField(Category2)

    def __unicode__(self):
        return self.name

class Protocol(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    date = models.DateTimeField('date published')
    materials = models.TextField(max_length=5000)
    methods = models.TextField(max_length=5000)
    tags = models.ManyToManyField(Tag)
    

    def __unicode__(self):
        return self.title

class ProtocolForm(ModelForm):
    class Meta:
        model = Protocol

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    about = models.TextField(max_length=5000)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
