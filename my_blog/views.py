from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import Post, Tag

import misaka


def starting_page(request):
    # fetches only 3 latest article on the basic of date.
    lastest_posts = Post.objects.all().order_by("-date")
    print(list(
        map(int, request.POST.getlist('bookmarkedPosts[]'))))
    return render(request, "my_blog/index.html", {
        "posts": lastest_posts,
        "bookmark_status": request.session.get("bookmarked", [])
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


def favourite_posts(request):
    # Retrieve all the bookmarked post IDs from the session
    bookmarked_ids = request.session.get("bookmarked", [])

    # Retrieve all posts corresponding to the bookmarked IDs
    posts = Post.objects.filter(id__in=bookmarked_ids)

    return render(request, "my_blog/favourites.html", {
        "posts": posts
    })


@csrf_exempt
def bookmark_page(request):
    if request.method == "POST":
        if "bookmarked" not in request.session:
            request.session["bookmarked"] = []

        bookmarked_posts = list(
            map(int, request.POST.getlist('bookmarkedPosts[]')))
        # print(bookmarked_posts)
        request.session["bookmarked"].extend(bookmarked_posts)
        request.session.save()
        response_body = {
            "status": "success",
            "bookmarked_posts": request.session["bookmarked"]
        }
        return JsonResponse(response_body)
    else:
        return HttpResponse("Method not allowed", status=405)
