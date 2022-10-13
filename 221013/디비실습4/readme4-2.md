views.py
profile이랑 follow 함수 추가
```py
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            # 내가(request.user) 그 사람의 팔로워 목록에 있다면
            # if me in you.followers.all():
            if you.followers.filter(pk=me.pk).exists():
                # 언팔로우
                you.followers.remove(me)
            else:
                # 팔로우
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

profile.html
```html
{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : {{ person.followers.all|length }} / 팔로잉 : {{ person.followings.all|length }}
  </div>


  {% if request.user != person %}
  <div>
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="언팔로우">
      {% else %}
        <input type="submit" value="팔로우">
      {% endif %}
    </form>
  <div>
  {% endif %}

  <h2>{{ person.username }}이 작성한 모든 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}이 작성한 모든 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}이 좋아요 한 모든 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <a href="{% url 'articles:index' %}">back</a>

{% endblock content %}
```

models.py
팔로우 받기 위해 추가
```py
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```


![image](./profile.png)
![image](./profile1.png)