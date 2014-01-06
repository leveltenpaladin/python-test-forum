from django.conf.urls import patterns, include, url
from django.contrib import admin
from forum import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^forum/', include('forum.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.landing_redirect),

)
