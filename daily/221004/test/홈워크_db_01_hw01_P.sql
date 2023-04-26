
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2)
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(3,'dolphin', 'carnivore', 210, 3),
(2, 'alligator', 'carnivore', 250, 50);


-- 3)
INSERT INTO zoo (name, eat, weight, age) VALUES
('dolphin', 'carnivore', 5,  3);

DELETE FROM zoo;
