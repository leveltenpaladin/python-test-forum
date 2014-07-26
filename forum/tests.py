from django.test import TestCase
from forum.models import Forum, User, Thread
from django.core.urlresolvers import reverse


class ForumModelTest (TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='rob', email='rob@blockoftext.com', password='top_secret')
        test = Forum.objects.create(name="test", creator=self.user)
        test2 = Forum.objects.create(name="test_2", parent=test, creator=self.user)
        Thread.objects.create(parent_forum=test2, title="test2", op=self.user)

    def test_get_number_of_threads(self):
        forum = Forum.objects.get(name="test")
        forum2 = Forum.objects.get(name="test_2")
        self.assertEqual(forum.get_number_threads(), 0)
        self.assertEqual(forum2.get_number_threads(), 1)

    def test_get_threads(self):
        forum = Forum.objects.get(name="test")
        forum2 = Forum.objects.get(name="test_2")
        self.assertEqual(len(forum.get_threads()), 0)
        self.assertEqual(len(forum2.get_threads()), 1)

    def test_get_sub_forum(self):
        forum = Forum.objects.get(name="test")
        forum2 = Forum.objects.get(name="test_2")
        self.assertEqual(forum.get_sub_forums()[0], forum2)

    def test_get_url(self):
        forum = Forum.objects.get(name="test")
        self.assertEqual(forum.get_absolute_url(), '/forum/1/')


class ForumViewTest (TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='rob', email='rob@blockoftext.com', password='top_secret')
        test = Forum.objects.create(name="test", creator=self.user)
        test2 = Forum.objects.create(name="test_2", parent=test, creator=self.user)
        test3 = Forum.objects.create(name="test_3", parent=test2, creator=self.user)
        Thread.objects.create(parent_forum=test2, title="test2", op=self.user)

    def test_landing_view(self):
        resp = self.client.get(reverse('landing'))
        self.assertEqual(resp.status_code, 200)

    def test_forum_detail_view(self):
        resp = self.client.get(reverse('forum_detail', kwargs={'pk': 2}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('forum' in resp.context)
        self.assertTrue(resp.context['forum'].name, 'test_2')
        self.assertTrue('parent' in resp.context)
        self.assertTrue(resp.context['parent'].name, 'test')
        self.assertTrue('threads' in resp.context)
        self.assertTrue(len(resp.context['threads']), 1)
        self.assertTrue('children' in resp.context)
        self.assertTrue(len(resp.context['children']), 1)

    def test_forum_detail_view_not_found(self):
        resp = self.client.get(reverse('forum_detail', kwargs={'pk': 2000}))
        self.assertEqual(resp.status_code, 404)
