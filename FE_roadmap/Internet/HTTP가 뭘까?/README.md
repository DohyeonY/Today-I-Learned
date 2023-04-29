### HTTP란 무엇일까?
- 클라이언트와 서버가 서로 통신하는 방법을 표준화하는 TCP/IP 기반 응용 프로그램 계층 통신 프로토콜입니다.
- 기본적으로 80포트를 사용하지만 다른 포트도 사용할 수 있다.
- HTTPS는 443 포트를 사용한다.

### 0.9 - 더 원 라이너(1991)
- HTTP의 첫 번째 문서화된 버전은 1991년 제안된 HTTP/0.9였습니다. 
- 이는 GET이라고 불리는 단일 방법을 가진 가장 간단한 프로토콜이었습니다. 
- 클라이언트가 서버의 웹 페이지에 엑세스해야 한다면 아래와 같은 간단한 요청을 했을 것 입니다.
```
GET /index.html
```
- 그리고 서버로부터의 응답은 다음과 같이 보였을 것입니다.
```
(response body)
(connection closed)
```
- 즉 서버는 요청을 받고 응답에 HTML로 응답하며 내용이 전송되는 즉시 연결이 닫힙니다.

### 1.0 - 1996
- HTTP/1.0은 이제 이미지, 비디오 파일, 일반 텍스트 또는 다른 콘텐츠 유형과 같은 다른 응답 형식을 처리할 수 있습니다.
    - 더 많은 메소드(POST 및 HEAD)
    - 요청 / 응답 형식 변경
    - 요청 및 응답 모두에 HTTP 헤더 추가
    - 응답 식별을 위한 상태 코드 추가
    - 문자 집합 지원 도입
    - 다중 파트 유형
    - 권한 부여
    - 캐싱
    - 콘텐츠 인코딩 등이 포함되어 있습니다.

- HTTP/1.0의 요청 및 응답은 다음과 같습니다.
```
GET / HTTP/1.0
Host: cs.fyi
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)
Accept: */*
```
```
응답 예입니다.
HTTP/1.0 200 OK 
Content-Type: text/plain
Content-Length: 137582
Expires: Thu, 05 Dec 1997 16:00:00 GMT
Last-Modified: Wed, 5 August 1996 15:55:28 GMT
Server: Apache 0.84

(response body)
(connection closed)
```
- 응답의 맨 처음에는 HTTP/1.0이 있고 다음에는 상태 코드 200과 이유 구문이 있습니다.