-- =========================================
-- DB: azienda_db (PostgreSQL)
-- =========================================

BEGIN TRANSACTION;

DROP TABLE IF EXISTS impiegati;
DROP TABLE IF EXISTS mansioni;
DROP TABLE IF EXISTS report_valori;

-- Mansioni: nome + range stipendio
CREATE TABLE mansioni (
  id              SERIAL PRIMARY KEY,
  nome            VARCHAR(100) NOT NULL UNIQUE,
  stipendio_min   NUMERIC(10,2) NOT NULL CHECK (stipendio_min >= 0),
  stipendio_max   NUMERIC(10,2) NOT NULL CHECK (stipendio_max >= stipendio_min)
);

-- Impiegati: matricola univoca + relazione verso mansioni
CREATE TABLE impiegati (
  matricola        INT PRIMARY KEY,
  nome             VARCHAR(120) NOT NULL,
  salario_mensile  NUMERIC(10,2) NOT NULL CHECK (salario_mensile >= 0),
  bonus_annuale    NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (bonus_annuale >= 0),
  mansione_id      INT NOT NULL REFERENCES mansioni(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- ReportValori: nessuna PK, coppie (descrizione, valore) aggiornate dai metodi
CREATE TABLE report_valori (
  descrizione  VARCHAR(120) NOT NULL,
  valore       NUMERIC(14,2) NOT NULL
);

-- Seed Mansioni
INSERT INTO mansioni (nome, stipendio_min, stipendio_max) VALUES
('Junior Developer', 1400.00, 2200.00),
('Senior Developer', 2500.00, 4500.00),
('HR',               1600.00, 3000.00),
('Sales',            1400.00, 3500.00);

-- Seed Impiegati (esempio)
INSERT INTO impiegati (matricola, nome, salario_mensile, bonus_annuale, mansione_id) VALUES
(1001, 'Mario Rossi', 1800.00, 500.00,  (SELECT id FROM mansioni WHERE nome='Junior Developer')),
(1002, 'Laura Bianchi', 3200.00, 0.00, (SELECT id FROM mansioni WHERE nome='Senior Developer')),
(1003, 'Giulia Verdi', 2100.00, 300.00, (SELECT id FROM mansioni WHERE nome='HR')),
(1004, 'Paolo Neri', 2000.00, 1200.00, (SELECT id FROM mansioni WHERE nome='Sales'));

-- Seed ReportValori (all'avvio)
INSERT INTO report_valori (descrizione, valore) VALUES
('TotaleStipendiMensili', 0.00),
('NumImpiegatiConBonus',  0.00);

COMMIT;