from django.shortcuts import (render, redirect)
from .forms import ContactForm
from blog.models import Blog
from services.models import Service

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    services = Service.objects.all()
    form = ContactForm()
    context = {
        'blogs': blogs,
        'services': services,
        'form': form
    }
    return render(request=request, template_name='index/index.html', context=context)


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        context = {
            'form': form
        }
    return redirect(to='/')