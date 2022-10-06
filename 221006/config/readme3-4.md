views.py

# 카운트세기 너무 어려워요 카운트어떻게 하는지까지 완료

```py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from .models import Question, Comment
from .forms import QuestionForm, CommentForm
import random

# Create your views here.
@require_safe
def index(request):
    eithers = Question.objects.order_by('-pk')
    context = {
        'eithers': eithers,
    }
    return render(request, 'eithers/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            either = form.save()
            return redirect('eithers:detail', either.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)


@require_safe
def detail(request, pk):
    either = get_object_or_404(Question, pk=pk)
    comment_form = CommentForm()
    comments = either.comment_set.all()

    questions = Question.objects.get(pk=pk)
    comm = questions.comment_set.all()

    red_num = comm.filter(pick=1).count()
    blue_num = comm.filter(pick=0).count()

    print(red_num)
    print(blue_num)

    context = {
        'either': either,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)


@require_POST
def delete(request, pk):
    either = get_object_or_404(Question, pk=pk)
    either.delete()
    return redirect('eithers:index')


@require_POST
def comments_create(request, pk):
    either = Question.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # comment.user = request.user
        comment.question_id = either
        comment.save()
    return redirect('eithers:detail', either.pk)

def random_page(request):
    entries = list(Question.objects.all())
    selected_page = random.choice(entries)
    return redirect('eithers:detail', selected_page.pk)

@require_POST
def comments_delete(request, question_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('eithers:detail', question_pk)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    either = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=either)
        if form.is_valid():
            form.save()
            return redirect('eithers:detail', either.pk)
    else :
        form = QuestionForm(instance=either)
    context = {
        'either': either,
        'form': form,
    }
    return render(request, 'eithers/update.html', context)
```

models.py

# 변경없음

```py
from secrets import choice
from django.db import models



# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField()
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

forms.py

# 변경없음

```py
from django import forms
from .models import Question, Comment



class QuestionForm(forms.ModelForm):
    issue_a = forms.CharField(label="RED TEAM")
    issue_b = forms.CharField(label="BLUE TEAM")
    

    class Meta:
        model = Question
        fields = '__all__'



class CommentForm(forms.ModelForm):

    pick = forms.ChoiceField(
        widget = forms.Select(),
        choices=([(1, 'RED TEAM'), (0, 'BLUE TEAM')]), 
                initial='3', required = True,)

    questions = Question.objects.values('pk')
    pklist = []
    for value in questions :
        pklist.append(value['pk'])
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude=('question_id',)


```

urls.py

# update delete commentdelete 추가

```py
from django.urls import path
from . import views

app_name = 'eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('random/', views.random_page, name='random_page'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]


```

index.html

# 모든 글들이 출력되게끔

```html
{% extends 'base.html' %}

{% block content %}

  <h1>INDEX</h1>
  <hr>
  {% for either in eithers %}
    <p>{{ either.pk }}번 이슈</p>
    <p><b>{{ either.title }}</b></p>
    <a href="{% url 'eithers:detail' either.pk %}">DETAIL</a>
    <hr>
  {% endfor %}
{% endblock content %}
```

detail.html

# 삭제랑 업데이트 추가

```html
{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <hr>

  <p><b>{{ either.title }}</b></p>
  <a href="{% url 'eithers:update' either.pk %}">UPDATE</a>
  <form action="{% url 'eithers:delete' either.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <p>Red TEAM</p>
  <p>==> {{ either.issue_a }}</p>
  <p>Blue TEAM</p>
  <p>==> {{ either.issue_b }}</p>
  
  <hr>
  <a href="{% url 'eithers:index' %}">BACK</a>
  <hr>

  <h4>댓글 작성</h4>
  <form action="{% url 'eithers:comments_create' either.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit" value='작성'>
  </form>
  <hr>

  <ul>

  <h4>댓글 목록</h4>
  {% for comment in comments %}

      {% if comment.pick == 1 %}
        <p>RED TEAM - {{ comment.content }}</p>
          <form action="{% url 'eithers:comments_delete' either.pk comment.pk %}" method="POST">
          {% csrf_token %} 
          <input type="submit" value="del"> 
         </form>
      {% else %}
        <p>BLUE TEAM - {{ comment.content }}</p>
          <form action="{% url 'eithers:comments_delete' either.pk comment.pk %}" method="POST"> 
            {% csrf_token %} 
          <input type="submit" value="del"> 
          </form>
      {% endif %}

    {% endfor %}

    </ul>


{% endblock content %}

```

create.html

# 변경 없음

```html
{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <a href="{% url 'eithers:index' %}">BACK</a>
  <hr>

  <form action="{% url 'eithers:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value='Create'>
  </form>
  <hr>

{% endblock content %}
```

![ima]()
