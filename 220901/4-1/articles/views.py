from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request) :
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request) :
        # 사용자의 데이터를 받아서
    # raise
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    # return redirect('articles:index',)
    return render(request, 'articles/create.html', )

def new(request) :
    return render(request, 'articles/new.html', )