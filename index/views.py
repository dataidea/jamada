from django.shortcuts import render
from .forms import ContactForm
from blog.models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'form': ContactForm
    }
    return render(request=request, template_name='index/index.html', context=context)


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request=request, template_name='index/index.html')