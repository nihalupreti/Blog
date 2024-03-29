from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_addr = models.EmailField(max_length=254)
    img = models.ImageField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.caption}'


class Genre(models.Model):
    genre = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    img_name = models.ImageField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.title} {self.date} {self.author} {self.tag}'
