from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(max_length=255, blank=True)
  author = models.ForeignKey(User, related_name='blog_posts')
  created = models.DateTimeField(auto_now_add=True)
  published = models.BooleanField(default=False)
  body = models.TextField()

  def __unicode__(self):
    return self.title

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)

  def url(self):
    return reverse('post', kwargs={'slug': self.slug})

class Tag(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100)