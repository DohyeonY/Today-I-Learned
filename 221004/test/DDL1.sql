CREATE TABLE zoo (
  name TEXT NOT NULL, 
  eat TEXT NOT NULL,
  weight INTEGER NOT NULL,
  height INTEGER,
  age INTEGER 
);

-- 동물들 데이터 입력
INSERT INTO zoo
VALUES 
  ('gorilla', 'omnivore', 215, 180, 5),
  ('rabbit', 'herbivore', 3, 150, NULL),
  ('tiger', 'carnivore', 220, 115, 3),
  ('elephant', 'herbivore', 3800, 280, 10),
  ('dog', 'omnivore', 8, 20, 1),
  ('eagle', 'carnivore', 8, 75, NULL),
  ('dolphin', 'carnivore', 210, NULL, 3),
  ('alligator', 'carnivore', 250, 50, NULL),
  ('panda', 'herbivore', 80, 90, 2),
  ('pig', 'omnivore', 70, 45, 5);

-- 동물들 이름과 키 데이터 조회
SELECT name, height FROM zoo;

-- 토끼 키 15로 수정 후 토끼 데이터 조회
UPDATE zoo
SET height=15
WHERE rowid = 2;

SELECT * FROM zoo
WHERE name LIKE 'rabbit';

-- 잡식 동물 데이터 삭제 후 전체 데이터 조회
DELETE FROM zoo
WHERE eat = 'omnivore';

SELECT * FROM zoo;