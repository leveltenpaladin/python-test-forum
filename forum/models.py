from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class ForumUser(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


class Forum(models.Model):
    parent = models.ForeignKey('Forum', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    creator = models.ForeignKey(User)
    status = models.IntegerField(default=0, null=False, blank=False)

    def get_number_threads(self):
        threads = self.get_threads()
        return threads.count()

    def get_threads(self):
        return Thread.objects.filter(parent_forum=self)

    def get_sub_forums(self):
        return Forum.objects.filter(parent=self)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/forum/%i/" % self.id


class Thread(models.Model):
    parent_forum = models.ForeignKey('Forum')
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=255)
    op = models.ForeignKey(User)
    status = models.IntegerField(default=0, null=False, blank=False)

    def __unicode__(self):
        return self.title

    def pretty_date(self):
        return self.created_date.strftime('%Y-%m-%d')

    def get_absolute_url(self):
        return "/forum/%i/%i" % (self.parent_forum.id, self.id)


class Reply(models.Model):
    parent = models.ForeignKey('Thread')
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User)
    content = models.TextField()
    status = models.IntegerField(default=0, null=False, blank=False)

    def __unicode__(self):
        return self.user.username

# Create your models here.
