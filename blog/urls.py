from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blogs'),
    path(route='', view=views.blogDetails, name='blog_details')
]