from telnetlib import STATUS
from django.shortcuts import render

from blog.models import Post
from django.views import generic

# Create your views here.

#create the blog view
class BlogView(generic.DetailView): 
    model = Post
    template_name = 'blog.html'

#create the about page
class AboutView(generic.TemplateView):
    template_name = 'about.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'