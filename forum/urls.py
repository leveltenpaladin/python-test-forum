from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from forum import views

urlpatterns = patterns('',
    url(r'^$', views.LandingView.as_view(), name='landing'),
    url(r'^(?P<pk>\d+)/$', views.ForumDetailView.as_view(), name='forum_detail'),
    url(r'^(?P<parent>\d+)/(?P<pk>\d+)/$', views.ThreadDetailView.as_view(), name='thread_detail'),
    url(r'^(?P<parent>\d+)/(?P<pk>\d+)/reply/$', login_required(views.ReplyCreationView.as_view()), name='thread_reply'),
    url(r'^login/$', views.LogInView.as_view(), name='login'),
    url(r'^logout/$', views.LogOutView.as_view(), name='logout'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^(?P<pk>\d+)/new-forum/$', login_required(views.ForumCreationView.as_view()), name='new_forum'),
    url(r'^(?P<pk>\d+)/new-topic/$', login_required(views.ThreadCreationView.as_view()), name='new_thread'),
)