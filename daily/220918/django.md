# Django
- [Django 설치 방법](#django-설치-방법)     
- [프로젝트](#프로젝트)
- [애플리케이션](#애플리케이션)

<br>
    
## django 디자인 패턴


### MTV 패턴
- MTV 패턴은 MVC 패턴을 기반으로 조금 변형된 패턴이다
```
MVC 패턴

Model - View - Controller의 준말
Model : 데이터와 관련된 로직을 관리
View : 레이아웃과 화면을 처리
Controller : 명령을 model과 view부분으로 연결
```

- 목적
```
더 나은 업무의 분리, 향상된 관리 제공
개발 효율성 및 유지보수가 쉬움
다수의 맴버로 개발하기 용이
```

- MTV 패턴 (장고)
```
Model : 데이터와 관련된 로직을 관리, 
        응용프로그램의 데이터 구조를 정의하고 데이터 베이스의 기록을 관리
Template : 레이아웃과 화면을 처리
           화면상의 사용자 인터페이스 구조와 레이아웃을 정의
View : Model & Template과 관련한 로직을 처리하는 응답을 반환
       클라이언트의 요청에 대해 처리를 분기하는 역할
```

### 요청과 응답
- render()
```
render(request, template_name, context,)
request : 응답을 생성한는데 사용되는 요청 객체
template_name : 템플릿의 전체 이름 또는 템플릿의 이름 경로
context : 템플릿에서 사용할 테이터(딕셔너리)
```

### Template
- django Template
```
테이터 표현을 제어하는 도구이자 표현에 관련된 로직
파이썬처럼 일부 프로그래밍 구조를 사용할 수 있지만 이것은 파이썬 코드로 실행되는게 아님
```

- Variable
```
변수명은 영어, 숫자와 밑줄의 조합으로 구성될 수 있으나 밑줄로는 시작 할 수 없음
ex) {{ variavle }}
```
- Filters
```
표시할 변수를 수정할 때 사용
ex) {{ name|lower }}
```
- Tags
```
출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등
변수보다 복잡한 일들을 수행
일부 태그는 종료 태그가 필요
ex) {% if %}{% endif %}
```

### 템플릿 상속     
- 코드의 재사용성에 초점
```
{% extends base.html %}
{% block content %}{% endblock %}
```
- 추가 템플릿 경로 추가하기
```
settings.py 에 TEMPLATES 부분에 DIRS : 부분을 수정
ex) [BASE_DIR / 'templates', ],
```    

### <form>
- 데이터가 전송되는 방법을 정의
- action = 어디, method = 어떤 방식
```
action
입력 데이터가 전송될 url을 지정
지정하지 않으면 데이터는 현재 form이 있는 페이지의 url로 보내짐
```
```
method
데이터를 어떻게 보낼 것인지 정의
2가지 방법밖에 없음 GET과 POST
```

### <input>
- 데이터를 사용자로부터 받기 위해 사용
- 기본값은 text

### <GET>
- 서버로부터 정보를 조회하는데 사용
- 데이터를 가져올때만 사용해야함
```
action
입력 데이터가 전송될 url을 지정
지정하지 않으면 데이터는 현재 form이 있는 페이지의 url로 보내짐
```
```
method
데이터를 어떻게 보낼 것인지 정의
2가지 방법밖에 없음 GET과 POST
```

### namespace
- urls.py 에 app_name = '앱이름' 적어주기
- url tag 의 변화
```
ex) {% url 'index' %} >> {% url 'articles:index' %}
```
```
method
데이터를 어떻게 보낼 것인지 정의
2가지 방법밖에 없음 GET과 POST
```
