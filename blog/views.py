from .models import Blog
from markdown import markdown
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog/blog.html', context)

def blogDetails(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    all_blogs = Blog.objects.all()
    context = {'blog':blog,
        'details':markdown(blog.body),
        'all_blogs':all_blogs}