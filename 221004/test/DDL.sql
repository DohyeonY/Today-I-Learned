CREATE TABLE animals (
  animal_name TEXT NOT NULL, 
  height INTEGER NOT NULL,
  weight INTEGER NOT NULL,
  age INTEGER 
);

-- meal 칼럼 추가
ALTER TABLE animals ADD COLUMN meal TEXT ;

-- animal_name 칼럼 이름 수정
ALTER TABLE animals RENAME COLUMN animal_name TO name;

-- 테이블 명칭 변경
ALTER TABLE animals RENAME TO zoo;

-- 테이블 삭제
DROP TABLE animals;