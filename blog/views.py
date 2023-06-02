from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/single-post.html")


def individual_post(request, slug):
    pass
