from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
    url(r'^$', views.landing, name='index'),
    url(r'^(\d+)/$', views.forum_detail),
    url(r'^(\d+)/(\d+)/$', views.thread_detail),
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
    url(r'^signup/$', views.signup),


)