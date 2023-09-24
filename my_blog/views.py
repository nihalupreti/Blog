from django.shortcuts import render



def starting_page(request):
    return render(request, "my_blog/index.html")

def single_post(request):
    pass

def all_posts(request):
    pass