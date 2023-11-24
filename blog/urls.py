from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blogs'),
    path(route='search/', view=views.search, name='search'),
    path(route='<int:blog_id>', view=views.blogDetails, name='blog_details')
]