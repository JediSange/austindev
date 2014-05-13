from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', 'website.views.home', name='home'),
  url(r'^about$', 'website.views.about', name='about'),
  url(r'^blog$', 'website.views.blog', name='blog'),
  url(r'^projects$', 'website.views.projects', name='projects'),
  url(r'^webdev$', 'website.views.webdev', name='webdev'),
)