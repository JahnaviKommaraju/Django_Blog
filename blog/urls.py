import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page, name="starting-page"),
    path("posts", views.posts,name="posts-page"),
    path("posts/<slug:slug>", views.post_detail,name="post-detail-page")  # here, <slug> -> it is for dynamic url eg: /posts/my-first-post
                               # here, <slug: slug> -> it is slug transformer
]
