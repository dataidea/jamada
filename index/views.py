from django.shortcuts import (render, redirect)
from .models import DisplayPicture
from .forms import ContactForm
from blog.models import Blog
from services.models import Service

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    services = Service.objects.all()
    display_picture = DisplayPicture.objects.all()[0]
    form = ContactForm()
    context = {
        'blogs': blogs,
        'services': services,
        'form': form,
        'display_picture': display_picture,
    }
    return render(request=request, template_name='index/index.html', context=context)


def contact(request):
    context = {}
    try: 
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context['message'] = 'Thanks for contacting me, I will get back to you as soon as possible.'
            return render(request=request, template_name='message.html', context=context)
        else:
            context['form'] = form
            context['message'] = 'Something went wrong while processing your form. Please try again or use other contact info provided'
            return render(request=request, template_name='message.html', context=context)
    except Exception as e:
        context['form'] = form
        context['message'] = f'Something went wrong while processing your form.\n {e} \n Please try again or use other contact info provided.'
        return render(request=request, template_name='message.html', context=context)