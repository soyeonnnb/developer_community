from django.urls import path
from . import views as snsapp_views

app_name = "snsapp"

urlpatterns = [
    path("", snsapp_views.home, name="home"),
    # 자유게시판
    path("board/", snsapp_views.BoardView.as_view(), name="board"),
    path("postcreate/", snsapp_views.postcreate, name="postcreate"),
    path("detail/<int:post_id>", snsapp_views.detail, name="detail"),
    path("new_comment/<int:post_id>", snsapp_views.new_comment, name="new_comment"),
    # 익명게시판
    path("an_board/", snsapp_views.AnBoardView.as_view(), name="an_board"),
    path("an_postcreate/", snsapp_views.an_postcreate, name="an_postcreate"),
    path("an_detail/<int:post_id>", snsapp_views.an_detail, name="an_detail"),
    path(
        "an_new_comment/<int:post_id>",
        snsapp_views.an_new_comment,
        name="an_new_comment",
    ),
]
