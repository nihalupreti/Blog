from django.forms import ModelForm,Textarea
from .models import Post

class ArticleForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["slug","tag"]
        widgets = {
            "title": Textarea(attrs={"placeholder":"Title"})
        }

        def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields["title"].widget.attrs.update({'class': 'form-control'})