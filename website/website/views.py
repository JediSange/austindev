from django.shortcuts import render_to_response

def home(request):
  return process_request(request, 'layouts/default.html')

def about(request):
  return process_request(request, 'pages/about.html')
  
def projects(request):
  return process_request(request, 'pages/projects.html')

def webdev(request):
  return process_request(request, 'pages/webdev.html')

# Helper function to pipe all render_to_response requests through
def process_request(request, layout, data=None, parent_url=None):
  # Safely initialize data
  if data is None:
    data = {}

  # Modify the path if a parent URL is provided for highlighting
  path = request.path
  if parent_url:
    path = parent_url

  # Build global data and pass to each response, modifying path as needed
  data['url'] = request.path
  data['side_nav'] = build_side_nav_links(path)

  return render_to_response(layout, data)

# Handles building the side nav and active states
def build_side_nav_links(path):
  # Define side links as list
  nav_links = [
    {'name': 'About', 'url': '/about', 'active': False},
    {'name': 'Blog', 'url': '/blog', 'active': False},
    {'name': 'Projects', 'url': '/projects', 'active': False},
    {'name': 'Web Dev', 'url': '/webdev', 'active': False},
  ]

  # Iterate over to see if any are active
  for index, link in enumerate(nav_links):
   if link['url'] == path:
     nav_links[index]['active'] = True

  return nav_links
