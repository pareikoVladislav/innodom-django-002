from django.contrib import admin
from news.models import News, Comment, Press

admin.site.register(Comment)
admin.site.register(Press)


def capitalize_title(modeladmin, request, queryset):
    for news in queryset:
        news.title = news.title.capitalize()
        news.save()


capitalize_title.short_description = 'Нормализовать заголовок'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'moderated')  # отображение доп полей
    list_filter = ('created_at',)  # фильтры для отображения записей
    search_fields = ('title', )  # фильтры для поиска записей
    actions = [capitalize_title]
