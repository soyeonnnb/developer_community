from .models import Post, Comment, AnPost, AnComment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs = {
            "class": "form-control",
            "placeholder": "제목을 입력해주세요",
            "rows": 20,
        }
        self.fields["body"].widget.attrs = {
            "class": "form-control",
            "placeholder": "내용을 입력해주세요",
            "rows": 20,
            "cols": 100,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]


class AnPostForm(forms.ModelForm):
    class Meta:
        model = AnPost
        fields = ["title", "body"]

    def __init__(self, *args, **kwargs):
        super(AnPostForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs = {
            "class": "form-control",
            "placeholder": "제목을 입력해주세요",
            "rows": 20,
        }
        self.fields["body"].widget.attrs = {
            "class": "form-control",
            "placeholder": "내용을 입력해주세요",
            "rows": 20,
            "cols": 100,
        }


class AnCommentForm(forms.ModelForm):
    class Meta:
        model = AnComment
        fields = ["comment"]
