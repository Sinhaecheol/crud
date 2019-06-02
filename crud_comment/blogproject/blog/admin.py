from django.contrib import admin
from blog.models import Article, Comment, Hashtag

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Hashtag)