from django.shortcuts import render_to_response

def home(request):
	return render_to_response('layouts/default.html')

def about(request):
  return render_to_response('pages/about.html')

def blog(request):
  return render_to_response('pages/blog.html')
  
def projects(request):
  return render_to_response('pages/projects.html')

def webdev(request):
  return render_to_response('pages/webdev.html')