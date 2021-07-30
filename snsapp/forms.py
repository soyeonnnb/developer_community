from .models import Post, Comment, AnPost, AnComment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]


class AnPostForm(forms.ModelForm):
    class Meta:
        model = AnPost
        fields = ["title", "body"]


class AnCommentForm(forms.ModelForm):
    class Meta:
        model = AnComment
        fields = ["comment"]
