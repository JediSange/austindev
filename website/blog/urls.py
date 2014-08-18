from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  url(r'^(/)?(?P<page>[-\w]*)$', 'blog.views.list', name='list'),
  url(r'/post/(?P<slug>[-\w]+)/$', 'blog.views.post', name='post'),
)