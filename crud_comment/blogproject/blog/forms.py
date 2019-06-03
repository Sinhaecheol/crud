from django import forms
from .models import Article, Comment, Hashtag
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "hashtags", "image"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['image']
