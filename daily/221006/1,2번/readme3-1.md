forms.py

# author 지우고 올리기

```py
from django import forms

from .models import Todo




class TodoForm(forms.ModelForm):



    class Meta:

        model = Todo

        # fields = '__all__'

        exclude = ('author',)
```

views.py

# create 기능 생성

```py
from django.shortcuts import render, redirect

from .models import Todo

from .forms import TodoForm

from django.views.decorators.http import require_http_methods



# Create your views here.

def index(request):

    todos = Todo.objects.order_by('-pk')

    context = {

        'todos': todos,

    }

    return render(request, 'todos/index.html', context)




@require_http_methods(['GET', 'POST'])

def create(request):

    if request.method == 'POST':

        form = TodoForm(request.POST)

        if form.is_valid():

            # 추가

            todo = form.save(commit=False)

            todo.author = request.user

            todo.save()

            # article = form.save()

            return redirect('todos:index')

    else:

        form = TodoForm()

    context = {

        'form': form,

    }

    return render(request, 'todos/create.html', context)
```

models.py

# 테이블 생성

```py
from django.db import models

from django.conf import settings



# Create your models here.



class Todo(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    completed = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
```

urls.py

# url 생성

```py
from django.urls import path

from . import views



app_name = 'todos'

urlpatterns = [

    path('', views.index, name='index'),

    path('create', views.create, name='create'),

]
```

create.html

# create html 생성

```html
{% extends 'base.html' %}



{% block content %}



  <h1>CREATE</h1>

  <form action="{% url 'todos:create' %}" method="POST">

    {% csrf_token %}

    {{ form.as_p }}

    <input type="submit">

  </form>

  <hr>

  <a href="{% url 'todos:index' %}">뒤로가기</a>

{% endblock content %}
```

index.html

# index html 생성 author - title 순으로 출력되게끔 해줌

```html
{% extends 'base.html' %}



{% block content %}

  <h1>Todo</h1>



  {% if request.user.is_authenticated %}

    <a href="{% url 'todos:create' %}">CREATE</a>



    <hr>

    {% for todo in todos %}

    <li>{{ todo.author }} - {{ todo.title }}</li>

    {% endfor %}



  {% else %}

  <hr>

   <p>작성된 글이 없습니다.</p>

  {% endif %}




{% endblock content %}
```

![image](./login.jpg)

![image](./create.jpg)

![image](./notlogin.jpg)
