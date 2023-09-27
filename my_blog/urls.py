from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="main-page"),
    path("posts", views.all_posts, name="all-post-page"),
    path("post/<slug:slug>", views.single_post, name="individual-post-page")
]
