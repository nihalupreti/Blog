from django.shortcuts import render
from .models import Post


def starting_page(request):
    # fetches only 3 latest article on the basic of date.
    lastest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "my_blog/index.html", {
        "posts": lastest_posts
    })


def single_post(request, slug):
    post = Post.objects.get(id=slug)
    return render(request, "my_blog/single_post.html", {
        "post_detail": post
    })


def all_posts(request):
    entire_posts = Post.objects.all()
    return render(request, "my_blog/all_posts.html", {
        "posts": entire_posts
    })
