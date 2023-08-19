from django.urls import path
from news.views import (
    all_news,
    create_news,
    update_news,
    all_comments,
    create_comment,
    update_comment
)

urlpatterns = [
    path("", all_news),
    path("add/", create_news),
    path("<int:news_id>/update/", update_news),
    path("comments/", all_comments),
    path("add_comment/", create_comment),
    path("update_comment/<int:comment_id>", update_comment),
]
