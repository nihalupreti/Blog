from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="landing_page"),
    path("posts", views.posts, name="post_page"),
    path("posts/<slug:slug>", views.individual_post, name="single_post_page")
]
