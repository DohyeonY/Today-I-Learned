from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request) :
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request) :
    if request.method == 'POST' :
        form = ArticleForm(request.POST)
        if form.is_valid() :
            article = form.save()
            return redirect('articles:detail', article.pk)
    else :
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return render(request, 'articles/index.html')

@require_safe
def detail(request, pk) :
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_POST
def delete(request, pk) :
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk) :
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' :
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)

    else :
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)