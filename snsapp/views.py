from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from snsapp.forms import PostForm
from .forms import CommentForm, PostForm, AnCommentForm, AnPostForm
from .models import Post, AnPost

# Home
def home(request):
    posts = Post.objects.filter().order_by("-date")[:10]
    an_posts = AnPost.objects.filter().order_by("-date")[:10]
    return render(request, "index.html", {"posts": posts, "an_posts": an_posts})


# 자유게시판
def board(request):
    posts = Post.objects.filter().order_by("-date")
    paginator = Paginator(posts, 10)
    page_num = request.GET.get("page")
    posts = paginator.get_page(page_num)
    return render(request, "board.html", {"posts": posts})


def postcreate(request):
    if request.method == "POST" or request.method == "FILES":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            finished_form = form.save(commit=False)
            finished_form.author = request.user
            finished_form.save()
            return redirect("snsapp:board")
    else:
        form = PostForm()
        return render(request, "post_form.html", {"form": form})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, "detail.html", {"post": post, "comment_form": comment_form})


def new_comment(request, post_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid:
        finished_form = comment_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.author = request.user
        finished_form.save()
    return redirect("snsapp:detail", post_id)


# 익명게시판


def an_board(request):
    posts = AnPost.objects.filter().order_by("-date")
    paginator = Paginator(posts, 10)
    page_num = request.GET.get("page")
    posts = paginator.get_page(page_num)
    return render(request, "board_an.html", {"posts": posts})


def an_postcreate(request):
    if request.method == "POST" or request.method == "FILES":
        form = AnPostForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("snsapp:an_board")
    else:
        form = AnPostForm()
        return render(request, "post_form_an.html", {"form": form})


def an_detail(request, post_id):
    post = get_object_or_404(AnPost, pk=post_id)
    comment_form = AnCommentForm()
    return render(
        request, "detail_an.html", {"post": post, "comment_form": comment_form}
    )


def an_new_comment(request, post_id):
    comment_form = AnCommentForm(request.POST)
    if comment_form.is_valid:
        finished_form = comment_form.save(commit=False)
        finished_form.post = get_object_or_404(AnPost, pk=post_id)
        finished_form.save()
    return redirect("snsapp:an_detail", post_id)
