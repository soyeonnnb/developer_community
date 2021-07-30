from django.contrib import admin
from .models import Post, Comment, AnPost, AnComment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(AnPost)
admin.site.register(AnComment)
