CREATE TABLE IF NOT EXISTS students
(
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    promo VARCHAR(50) NOT NULL,
    views INTEGER NOT NULL DEFAULT 0
);

INSERT INTO students (nom, promo, views) VALUES
('Tima bel', 'M1 Info', 15),
('Fatima bou', 'M1 Info', 16),
('Sonia chi', 'M1 Info', 17);
