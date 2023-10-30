from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="main-page"),
    path("favourites", views.favourite_posts, name="my-favourite"),
    path("bookmark", views.bookmark_page),
    path("posts/<str:tags>", views.all_posts, name="all-post-page"),
    path("post/<slug:slug>", views.single_post, name="individual-post-page")
]
