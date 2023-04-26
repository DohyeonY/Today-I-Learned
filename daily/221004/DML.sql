CREATE TABLE users (
  first_name TEXT NOT NULL, 
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- 이름과 나이 조회
SELECT first_name, age 
FROM users;

-- 전체 조회
SELECT * FROM users;

-- rowid 조회
SELECT rowid, first_name
FROM users;

-- order by 나이가 어린순
SELECT first_name, age FROM users
ORDER BY age ASC;

-- order by 나이가 많은순
SELECT first_name, age FROM users
ORDER BY age DESC;

-- order by 나이가 어린순 + 계좌잔고 많은순
SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;

-- distinct 중복없이 모든 지역 조회
SELECT DISTINCT country FROM users;

-- distinct 지역순으로 내림차순 중복없이 모든 지역 조회
SELECT DISTINCT country FROM users
ORDER BY country;

-- distinct 이름과 지역이 중복 없이 모든 이름과 지역 조회
SELECT DISTINCT first_name, country FROM users;

-- distinct 이름과 지역이 중복 없이 지역순으로 내림차순으로 모든 이름과 지역 조회
SELECT DISTINCT first_name, country FROM users
ORDER BY country DESC;

-- where 나이가 30 이상인 사람들의 이름 나이 계좌 조회
SELECT first_name, age, balance FROM users
WHERE age >= 30;

-- where 나이가 30 이상이고 잔고 50이상인 사람들의 이름 나이 계좌 조회
SELECT first_name, age, balance FROM users
WHERE age >= 30 AND balance > 500000;

-- like 이름에 호가 있는 사람들 이름 성 조회
SELECT first_name, last_name FROM users
WHERE first_name LIKE '%호%';

-- like 이름이 준으로 끝나는 사람들 이름 성 조회
SELECT first_name, last_name FROM users
WHERE first_name LIKE '%준';

-- like 서울 지역 전화번호인 사람들 이름 전화번호 조회
SELECT first_name, phone FROM users
WHERE phone LIKE '02%';

-- like 나이가 20대인 사람들의 이름과 나이 조회
SELECT first_name, age FROM users
WHERE age LIKE '2_';

-- like 전화번호 중간이 51로 시작하는 이름과 전화번호 조회
SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';

-- like 경기도 혹은 강원도에 사는 사람들 조회
SELECT first_name, country FROM users
WHERE country = '경기도' OR country = '강원도';

SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도');

-- like 경기도 혹은 강원도에 살지 않는 사람들
SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강원도');

-- between 나이가 20살 이상 30살 이하인 사람들
SELECT first_name, age FROM users
WHERE age BETWEEN 20 AND 30;

-- between 나이가 20살 이상 30살 이하가 아닌 사람들
SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 AND 30;

-- limit 첫번째부터 열번째까지 rowid 이름 조회
SELECT rowid, first_name FROM users
LIMIT 10;

-- limit 계좌잔고 많은 10명의 이름과 잔고 조회
SELECT first_name, balance FROM users
ORDER BY balance DESC
LIMIT 10;

-- limit 나이가 가장 어린 5명
SELECT first_name, age FROM users
ORDER BY age 
LIMIT 5;

-- offset 11번째부터 20번째까지 rowid 까지 출력
SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;

-- groupby 각 지역별로 몇 명이 살고있느지 조회
SELECT country, COUNT(*) AS number_of_people FROM users
GROUP BY country;

-- 유저테이블 전체 행 수 조회
SELECT COUNT(*) FROM users;

-- 나이가 30살 이상인 사람들의 나이평균
SELECT AVG(age) FROM users WHERE age >= 30;


-- CREATE
CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO classmates
VALUES ('홍길동', 23, '서울');

-- insert 다수넣기
INSERT INTO classmates
VALUES 
  ('김철수', 30, '경기'),
  ('이영미', 31, '강원'),
  ('박진성', 26, '전라'),
  ('최지수', 12, '충청'),
  ('정요한', 28, '경상');

-- update
UPDATE classmates
SET name='김철수한무두루미',
address='제주도'
WHERE rowid = 2;


-- delete 5번 삭제
DELETE FROM classmates
WHERE rowid = 5;

-- 삭제된것 확인
SELECT rowid, * FROM classmates;
