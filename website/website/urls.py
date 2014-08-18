from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
  #Static links
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', 'website.views.home', name='home'),
  url(r'^about$', 'website.views.about', name='about'),
  url(r'^projects$', 'website.views.projects', name='projects'),
  url(r'^webdev$', 'website.views.webdev', name='webdev'),

  #Sub modules
  url(r'^blog', include('blog.urls'), name='blog'),
)