# 현재 프로젝트
- woopolemong
- 목표기간: 12월
---
## 팀원
- 김태영
- 김희현
- 심재원
- 여도현
- 정원재
- 최유경
## 사용 
- 파이썬, 장고, 부트스트랩
---
# 계획
1. 주제 선정 (완료)
2. 기능 명세 (완료)
3. 템플릿 선정 (완료)
4. UI - 와이어프레임 (진행 중)
5. DB설계
6. API 설계
7. 구현
---

# 1. 주제
- 토이프로젝트 포트폴리오를 올릴 웹사이트
<p></p>

---
# 2. 기능 명세
1. 로그인 페이지
    - 아이디, 비번 입력 창, 로그인 버튼
    - 장고 DB를 이용해 진행
    - 아이디 찾기, 비밀번호 찾기, 회원가입 링크
    - 혹은 장고 기본 템플릿 활용
<p></p>

2. 비밀번호 찾기 페이지
    - 아이디, 이메일 입력
    - 이메일이 일치하면 인증번호 전송
    - 일정 시간 내에 인증번호 입력 후 버튼 클릭
    - 비밀번호 수정 페이지로 이동
    - 혹은 장고 기본 템플릿 활용
<p></p>

3. 회원가입 페이지
    - 아이디
        - 중복확인 버튼
    - 비밀번호, 비밀번호 확인
    - 이메일
        - 중복확인
        - 이메일로 인증번호 전송
        - 일정 시간내에 입력으로 인증
    - 혹은 장고 기본 템플릿 활용
<p></p>

4. Nav) 로고, 소개, 프로젝트(포트폴리오), 갤러리, 로그인(회원가입) / 아이디(회원정보)
<p></p>

5. 소개 페이지(index 페이지)
    - 팀원이름, 약력, 인사말, 포트폴리오게시판링크 문의하기까지
<p></p>

6. 프로젝트(포트폴리오) 게시판
    - 누구나 상세페이지 조회 가능
    - 시간순, 추천순, 조회순으로 정렬
    - 로그인한 경우만 글쓰기 가능
<p></p>

7. 상세페이지
    - 좌측: 사진
    - 우측 제목, 내용
    - 수정(링크)
    - 삭제(링크)
        - 삭제 시 두 번이상 페이지를 넘어가며 확인해야함
    - 내부적으로 글 작성 시간 및 수정 시간 입력되어 있어야함

8. 글쓰기 및 수정 페이지
    - 대표사진 입력란
    - 각 사진 입력란
    - 사진의 제목
    - 사진의 내용
    - 수정 페이지의 경우 각 칸에 기존의 내용 입력되어있어야함
    - 글쓰기, 수정 버튼
<p></p>

9. 회원 정보
    - 장고 기본 템플릿 활용

---
# 3. 템플릿
베이스 템프릿:
https://ko.wix.com/website-template/view/html/1885?originUrl=https%3A%2F%2Fko.wix.com%2Fwebsite%2Ftemplates%2Fhtml%2Fdesign%2Fgraphic-web&tpClick=view_button&esi=146eecae-f886-4b3c-8cc6-b987710b27af

---
# 4. UI - 와이어프레임
- 인덱스: 김태영
- 네비, 푸터, 상세페이지: 여도현
- 로그인: 최유경
- 프로젝트 게시판: 심재원
- 회원가입: 정원재
- 게시글 작성(수정): 김희현
- 사용 툴: figma https://www.figma.com/
- 사용 색: https://kr.123rf.com/photo_73941714_%EC%9B%B9-%EC%82%AC%EC%9D%B4%ED%8A%B8-%ED%85%9C%ED%94%8C%EB%A6%BF-%ED%95%9C-%ED%8E%98%EC%9D%B4%EC%A7%80-%EB%94%94%EC%9E%90%EC%9D%B8-%ED%97%A4%EB%8D%94-%EB%B0%8F-%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4-%EC%9A%94%EC%86%8C-%EC%97%AC%ED%96%89%EC%82%AC-%EC%97%B4%EB%8C%80-%EC%97%AC%EB%A6%84-%EB%A6%AC%EC%A1%B0%ED%8A%B8-.html
스포이드 - 최유경
<p></p>

- 참조 사이트
    - figma: https://www.figma.com/
    - whimsical: https://whimsical.com/
    - 링크 모음: https://time-click-b2a.notion.site/bb132b78a4854fe581390a96bc31429b
---
# 5. DB설계
- Django model.py에 들어갈 내용 설계
- 참조 사이트
    - erdcloud: https://www.erdcloud.com/
---
# 6. API 설계
- Django urls.py, views.py에 들어갈 내용 설계
---
# 7. 구현
- Django, html, css, bootstrap으로 열심히 구현
- 추후 DB, js, Vue 등을 배우면 더 이쁘게 만들어 봅시다.


---
# 참고 사이트
- https://velog.io/@qwe6293/series/%ED%86%A0%EC%9D%B4%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-Tre
- https://velog.io/@jake0601/%EB%B8%94%EB%A1%9C%EA%B7%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-1
