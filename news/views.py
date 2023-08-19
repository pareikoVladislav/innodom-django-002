from django.shortcuts import render, redirect, get_object_or_404

from news.forms import CreateNewsForm, NewsUpdateForm, CommentUpdateForm, CommentForm
from news.models import News, Comment


def hello_world(request):
    context = {
        "greeting_message": "Hello from Django Templates!!!"
    }

    return render(request, "news/templates/home.html", context)


def all_news(request):
    news = News.objects.all()

    context = {
        "news": news
    }

    return render(request, "news/templates/news.html", context)


def create_news(request):
    if request.method == 'POST':
        form = CreateNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            new_news = News.objects.create(
                title=title,
                description=description
            )

            return redirect(all_news)
        context = {"form": form}

    else:
        form = CreateNewsForm()
        context = {"form": form}

    return render(
        request,
        "news/templates/create_news.html",
        context
    )


def update_news(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if request.method == "POST":
        form = NewsUpdateForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect(all_news)

        context = {"form": form}

    else:
        form = NewsUpdateForm(instance=news)

        context = {"form": form}

    return render(
        request,
        "news/templates/update_news.html",
        context
    )


def all_comments(request):
    comments = Comment.objects.all()

    context = {
        "comments": comments,
    }

    return render(request, "news/templates/comments.html", context)


def create_comment(request):
    news_queryset = News.objects.filter(moderated=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect(all_comments)

    else:
        form = CommentForm()

    context = {
        "form": form,
        "news": news_queryset,
    }

    return render(
        request,
        "news/templates/create_comment.html",
        context
    )


def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentUpdateForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(all_comments)

    else:
        form = CommentUpdateForm(instance=comment)

    context = {"form": form}

    return render(
        request,
        "news/templates/update_comment.html",
        context
    )
