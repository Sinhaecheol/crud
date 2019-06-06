from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm, HashtagForm

# Create your views here.
def main(request):
    articles = Article.objects.all()
    hashtags = Hashtag.objects.all()
    medias = Article.objects
    return render(request, 'blog/main.html', {'articles':articles, 'hashtags': hashtags, 'medias': medias})

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
                comment = form.save(commit=False) #아직 저장x
                comment.article = article # 모델에서 객체를 받기로함
                comment.content = form.cleaned_data["content"] #내용을 입력해라
                comment.save() # 저장
                return redirect("blog:detail", article_id) #aritcle_id로 참조하고 디테일페이지로 감
    else:
        form = CommentForm()
        return render(request, "blog/detail.html", {"article":article, "form":form})


def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.title = form.cleaned_data["title"]
            article.content = form.cleaned_data["content"]
            article.published_at = timezone.now()
            article.save()
            form.save_m2m()
            return redirect("blog:main")
    else:
        form = ArticleForm()
        return render(request, "blog/new.html", {'form':form})

def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if ("image" in request.FILES) and ("image-clear" in request.POST):
            del request.FILES["image"]
        if form.is_valid():
            article = form.save(commit=False)
            article.title = form.cleaned_data["title"]
            article.content = form.cleaned_data["content"]
            article.published_at = timezone.now()
            article.save()
            return redirect("blog:detail", article.id)
    else:
        form = ArticleForm(instance=article)
        return render(request, "blog/new.html", {'form':form})

def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("blog:main")

def comment_delete(request, article_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id) #id또는 pk
        comment.delete()
        return redirect("blog:detail", article_id)

# def comment_delete(request, comment_id):
#         comment = get_object_or_404(comment, comment_id)
#         article_id = comment.article.id
#         comment.delete()
#         return redirect("blog:detail", article_id)

# def comment_delete(request, comment_id):
#         comment = get_object_or_404(comment, comment_id)
#         comment.delete()
#         return redirect("blog:detail", comment.article.id)
# 2,3번 방법으로 하면 article_id는 안넘겨주어도 괜찮음

def comment_edit(request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                    comment = form.save(commit=False)
                    comment.content = form.cleaned_data["content"]
                    comment.save()
                    return redirect("blog:detail", comment.article.id)
        else:
            form = CommentForm(instance=comment) #기본으로 정해주는 값을 지정해주는거
            return render(request, "blog/new.html", {"form":form})

def hashtagform(request, hashtag=None):
        if request.method == 'POST':
                form = HashtagForm(request.POST, instance=hashtag)
                if form.is_valid():
                        hashtag = form.save(commit=False)
                        if Hashtag.objects.filter(name=form.cleaned_data['name']):
                                form = HashtagForm()
                                error_message = "이미 존재하는 해시태그 입니다."
                                return render(request, 'blog/hashtag.html', {'form': form, "error_message": error_message})
                        else:
                                hashtag.name = form.cleaned_data['name']
                                hashtag.save()
                                return redirect('blog:main')
        else:
                form = HashtagForm(instance=hashtag)
                return render(request, 'blog/hashtag.html', {'form': form})

def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'blog/search.html', {'hashtag': hashtag})
