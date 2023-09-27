from django.shortcuts import render
from .models import Post



def starting_page(request):
    lastest_posts = Post.objects.all().order_by("-date")[:3]  #fetches only 3 latest article on the basic of date.
    return render(request, "my_blog/index.html", {
        "posts" : lastest_posts
    })

def single_post(request):
    pass

def all_posts(request):
    entire_posts = Post.objects.all()
    return render(request, "my_blog/all_posts.html", {
        "posts" : entire_posts
    })