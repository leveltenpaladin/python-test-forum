from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Forum(models.Model):
    parent = models.ForeignKey('Forum', blank=True, null=True, on_delete=models.SET_NULL, related_name='child_forums')
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name='created_forums')
    status = models.IntegerField(default=0, null=False, blank=False)

    def get_number_threads(self):
        threads = self.get_threads()
        return threads.count()

    def get_threads(self):
        return self.threads.all()

    def get_sub_forums(self):
        return self.child_forums.all()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum_detail', args=[self.id])

    @staticmethod
    def get_root_forums():
        return Forum.objects.filter(parent=None)


class Thread(models.Model):
    parent_forum = models.ForeignKey('Forum', related_name='threads')
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    op = models.ForeignKey(User)
    status = models.IntegerField(default=0, null=False, blank=False)

    def __unicode__(self):
        return self.title

    def pretty_date(self):
        return self.created_date.strftime('%Y-%m-%d')

    def get_absolute_url(self):
        return reverse('thread_detail', args=[self.parent_forum.id, self.id])

    def get_replies(self):
        return self.replies.all()


class Reply(models.Model):
    parent = models.ForeignKey('Thread', related_name='replies')
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    content = models.TextField()
    status = models.IntegerField(default=0, null=False, blank=False)

    def pretty_date(self):
        return self.created_date.strftime('%Y-%m-%d')

    def __unicode__(self):
        return self.user.username
