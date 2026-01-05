CREATE TABLE IF NOT EXISTS students
(
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    promo VARCHAR(50) NOT NULL,
    notes FLOAT
);

INSERT INTO students (nom, promo, notes) VALUES
('Tima bel ', 'M1 Info', 15),
('Fatima bou', 'M1 Info', 16),
('Sonia chi', 'M1 Info', 17);
