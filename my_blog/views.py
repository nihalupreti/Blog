from django.shortcuts import render
from .models import Post, Tag

import misaka


def starting_page(request):
    # fetches only 3 latest article on the basic of date.
    lastest_posts = Post.objects.all().order_by("-date")
    return render(request, "my_blog/index.html", {
        "posts": lastest_posts
    })


def single_post(request, slug):
    post = Post.objects.get(id=slug)
    all_posts = Post.objects.all().order_by("-date")
    post.content = misaka.html(post.content)
    tag = list(post.tag.all().values_list("caption", flat=True))
    return render(request, "my_blog/single_post.html", {
        "post_detail": post,
        "tags": tag,
        "all_posts": all_posts
    })


def all_posts(request, tags):
    all_tags = Tag.objects.all()
    if (tags != "all"):
        post_by_tags = Post.objects.filter(tag__caption=tags)
        return render(request, "my_blog/all_posts.html", {
            "posts": post_by_tags,
            "tags": all_tags,
        })
    else:
        entire_posts = Post.objects.all()
        return render(request, "my_blog/all_posts.html", {
            "posts": entire_posts,
            "tags": all_tags,
        })
