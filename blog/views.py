from .models import Blog
from markdown import markdown
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog/blog.html', context)

def blogDetails(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    all_blogs = Blog.objects.all()[:2]
    context = {'blog':blog,
        'body':markdown(blog.body),
        'all_blogs':all_blogs}
    
    return render(request=request, template_name='blog/blog_details.html', context=context)


def search(request):
    query = request.POST.get(key='query')
    blogs = Blog.objects.filter(
        Q(title__icontains=query) |
        Q(body__icontains=query)
    )

    context = {'blogs': blogs}
    template_name = 'blog/blog.html'
    return render(request=request, template_name=template_name, context=context)