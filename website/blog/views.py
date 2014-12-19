from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

def list(request, page):
  # Get all posts, reverse sorted by creation date
  posts = Post.objects.all().order_by('-created')
  
  # Filter out unpublished posts if not admin
  if not request.user.is_superuser:
    posts = posts.filter(published=True)

  # Attempt to get the current page, default to 1
  paginator = Paginator(posts, 5)
  try:
    posts = paginator.page(page)
  except PageNotAnInteger, EmptyPage:
    posts = paginator.page(1)
    
  # Finally, pass the data to the template
  params = {}
  params['page'] = page
  params['posts'] = posts
  return render_to_response('list.html', params)

def post(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render_to_response('post.html', {'post': post})