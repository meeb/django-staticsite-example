from django.urls import path
from .views import IndexView, PostView, TagView
from .models import Post, Tag


def get_index():
    return None


def get_posts():
    for post in Post.objects.published():
        yield {'slug': post.slug}


def get_tags():
    for tag in Tag.objects.all():
        yield {'tag': tag.name}


urlpatterns = [

    path('',
        IndexView.as_view(),
        name='blog-index',
        staticsite_path=True,
        staticsite_urls_generator=get_index,
        staticsite_filename='index.html'),

    path('post/<slug:slug>.html',
        PostView.as_view(),
        name='blog-post',
        staticsite_path=True,
        staticsite_urls_generator=get_posts),

    path('tag/<slug:tag>.html',
        TagView.as_view(),
        name='blog-tag',
        staticsite_path=True,
        staticsite_urls_generator=get_tags),

]
