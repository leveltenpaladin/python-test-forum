from django.test import TestCase
from forum.models import Forum, User, Thread


class ForumTestCase (TestCase):

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
