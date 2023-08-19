from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(
        'News',
        on_delete=models.CASCADE,
        limit_choices_to={"moderated": True},
        related_name="news"
    )
    context = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    moderated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}-{self.context[:11]}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class News(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="News_title",
        help_text="Must contain only 100 symbols",
        unique_for_date="created_at"
    )
    description = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    moderated = models.BooleanField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['created_at']


class Press(models.Model):
    name = models.CharField(max_length=75)
    news = models.ManyToManyField(News)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Press'
        verbose_name_plural = 'Press'
