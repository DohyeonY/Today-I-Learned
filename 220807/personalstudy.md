f1. 시맨틱 태그
  요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
  검색엔진 최적화를 위해 메타태그, 시맨틱 태그 등을 통한 마크업을 활용

2. 
  <a></a> 하이퍼링크
  <b></b> 굵은 글씨 요소
  <strong></strong> 중요한 강조하고자 하는 요소
  <i></i> 기울임 글씨 요소
  <em></em> 중요한 강조하고자 하는 요소
  <br> 엔터넣기
  <img> 이미지 넣기 href 부분이 소스
  <span></span> 의미없는 인라인 컨테이너
  <p></p> 하나의 문단
  <hr> 수평선 하나 생기기
  <ol></ol> 순서가 있는 리스트
  <ul></ul> 순서가 없는 리스트
  <pre></pre> html에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백문자를 유지
  <blockquote></blockquote> 텍스트가 긴 인용문 주로 들여쓰기를 한 것으로 표현됨
  <div></div> 의미없는 블록 레벨 컨테이너

3. <form> 정보데이터를 서버에 제출하기 위해 사용하는 태그
  action : form을 처리할 서버의 url
  method : form을 제출할 때 사용할 http 메서드
  enctype : method가 post인 경우 데이터의 유형
  ex) <form action="/search" method="GET"></form>

4. <input> 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
  대표속성 : name, value, required, readonly, autofocus, autocomplete, disabled
  ex) <form action="/search" method="GET">
        <input type="text" name="q"></form>

4-1. <label> 
  라벨은 input자체의 초점으 맞추거나 활성화 시킬 수 있음
    - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서도 편하게 사용가능
    - 라벨과 인풋 임력의 관계까 시각적 뿐 아니라 화면리더기에서도 라벨을 읽어 쉽게 내용 확인이 가능
  인풋에 id속성을, 라벨에 for 속성을 활용하여 상호 연관을 시킴
  ex) <label for="agreement">개인정보 수집에 동의합니다.</label>
      <input type="checkbox" name="agreement" id="agreement">

4-2. <input> 유형
  text : 일반 텍스트 입력
  password : 입력 시 값이 보이지 않는 별표로 표기
  email : 이메일 형식이 아니면 제출 불가
  number : min,max,step 속성을 활용하여 숫자 범위 설정 가능
  file : accept 속성을 활용하여 파일 타입 지정 가능

  (항목 중 선택)
  checkbox : 다중 선택
  radio : 단일 선택

  (기타)
  color : 색 선택
  date : 날짜 선택
  hidden : 사용자에게 보이지 않는 input

  참고 : http://developer.mozilla.org/ko/docs/Web/HTML/Element/Input

5. CSS
  선택자 h1  선언 color:blue; 속성font-size: 값 15px;
    h1{
    color: blue;
    font-size: 15px;
  }
  정의 방법 
  - 인라인 : 해당 태그에 직접 style 속성을 활용
    <h1 style="color:blue; font-size: 100px;">hello</h1>
  - 내부 참조 : <head> 태그 내에 <style>에 지정
    <style>
      h1{
        color:blue;
        font-size: 100px;
      }
      </style>
  - 외부 참조(가장 많이 쓰는 방식) : 외부 CSS파일을 <head>내 <link>를 통해 불러오기

6. CSS Selectors
  클래스 선택자 : .div
  id 선택자 : #div
  자식 결합자 : .div > p
  자손 결합자 : .div p
  전체 선택자 : *
  요소 선택자 : div

6-1. CSS 적용 우선순위
  !important - 인라인 - id - class, 속성, pseudo-class - 요소, pseudo-element

7. CSS 기본 스타일
   em : 상속영향 받음, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
  
   rem : 상속 영향 안받음, 최상위 요소의 사이즈를 기준으로 배수 단위를 가짐




