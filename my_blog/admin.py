from django.contrib import admin
from .models import Author, Tag, Post, Genre


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author")
    list_filter = ["date", "author", "tag"]


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Genre)
