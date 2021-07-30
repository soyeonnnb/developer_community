from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# 자유게시물 모델
class Post(models.Model):

    """Post Definition"""

    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


# 익명게시물 모델
class AnPost(models.Model):

    """AnPost Definition"""

    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AnComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(AnPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
