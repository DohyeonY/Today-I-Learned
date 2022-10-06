views.py

# 허가된사람 아니면 로그인페이지로 가게끔 아니면 하고 삭제

# booleanfield 에 값이 0 혹은 1 만들어가서 0이면 1로 1이면 0으로 스위치

```py
@require_POST

def delete(request, pk):

    if not request.user.is_authenticated:

        return redirect('accounts:login')



    todo = get_object_or_404(Todo, pk=pk)



    if todo.author == request.user:

        todo.delete()



    return redirect('todos:index')

@require_POST

def toggle(request, pk):

    todo = Todo.objects.get(pk=pk)

    if todo.completed == 0:

        todo.completed = 1

        todo.save()

    else :

        todo.completed = 0

        todo.save()

    return redirect('todos:index')
```



models.py

# booleanfield 추가

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

# url추가

```py
from django.urls import path

from . import views



app_name = 'todos'

urlpatterns = [

    path('', views.index, name='index'),

    path('create/', views.create, name='create'),

    path('<int:pk>/delete/', views.delete, name='delete'),

    path('toggle/<int:pk>', views.toggle, name='toggle'),

]
```

index.html

# 만약 값이 있으면(1) 취소하기가 출력되고 값이 없으면(0) 완료하기가 출력되게끔 버튼 만들기

```html
{% extends 'base.html' %}



{% block content %}

  <h1>Todo</h1>



  {% if request.user.is_authenticated %}

    <a href="{% url 'todos:create' %}">CREATE</a>



    <hr>

    {% for todo in todos %}

    <li>{{ todo.author }} - {{ todo.title }}</li>



      {% if request.user == todo.author %}



        {% if todo.completed %}

        {% comment %} <button>완료하기</button> {% endcomment %}

          <form action="{% url 'todos:toggle' todo.pk %}" method="POST">

          {% csrf_token %}

          <button>취소하기</button>

        </form>

        {% else %}

        {% comment %} <button>취소하기</button> {% endcomment %}

        <form action="{% url 'todos:toggle' todo.pk %}" method="POST">

          {% csrf_token %}

          <button>완료하기</button>

        </form>

        {% endif %}



      <form action="{% url 'todos:delete' todo.p %}" method="POST">

        {% csrf_token %}

        <button>삭제하기</button>

      </form>

      {% endif %}

    {% endfor %}



  {% else %}

  <hr>

   <p>작성된 글이 없습니다.</p>

  {% endif %}




{% endblock content %}
```

![image](C:\Users\multicampus\AppData\Roaming\marktext\images\1c2670c7e5a2db557ba8fb3cf34ebbe6bb14a197.jpg)

![image](C:\Users\multicampus\AppData\Roaming\marktext\images\adb79b903ed3be197fa9802bc9aa1764b2cf7ecd.jpg)

![image](C:\Users\multicampus\AppData\Roaming\marktext\images\8b1f1f40883a35d6b577ffa0e0843e29f1212833.jpg)
