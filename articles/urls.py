from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("health/", views.health, name="health"),

    path(
        "articles/",
        views.article_list,
        name="article_list"
    ),

    path(
        "articles/<int:id>/",
        views.article_detail,
        name="article_detail"
    ),
    path(
        "articles/<int:id>/edit/",
        views.article_update,
        name="article_update"
    ),
    path(
        "articles/<int:id>/delete/",
        views.article_delete,
        name="article_delete"
    ),

    path(
        "generateArticle/",
        views.generateArticle,
        name="generateArticle"
    ),
    path(
        "article-chat/",
        views.article_chat,
        name="article_chat"
    ),
    path(
    "save-article/",
    views.save_article,
    name="save_article"
    ),

    path(
        "AboutUs/",
        views.about,
        name="AboutUs"
    ),

    path(
        "ContactUs/",
        views.contact,
        name="ContactUs"
    ),
]