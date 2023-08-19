from django import forms

from news.models import News, Comment


class CreateNewsForm(forms.Form):
    class Meta:
        model = News
        fields = ['title', 'description']

    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=3000)


class NewsUpdateForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'description', 'moderated']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['context', 'news']

    context = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        max_length=1500
    )
    news = forms.ModelChoiceField(queryset=News.objects.filter(moderated=True))


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['context', 'moderated']
