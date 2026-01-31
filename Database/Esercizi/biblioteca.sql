-- =========================
-- TESSERE
-- =========================
CREATE TABLE tessere (
  id          BIGSERIAL PRIMARY KEY,
  codice      VARCHAR(50) NOT NULL UNIQUE,
  importo     NUMERIC(10,2) NOT NULL DEFAULT 0.00,
  attiva      BOOLEAN NOT NULL DEFAULT TRUE,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMPTZ NULL
);

-- =========================
-- UTENTI
-- =========================
CREATE TABLE utenti (
  id          BIGSERIAL PRIMARY KEY,
  nome        VARCHAR(100) NOT NULL,
  cognome     VARCHAR(100) NOT NULL,
  tipo        VARCHAR(20) NOT NULL CHECK (tipo IN ('STUDENTE','DOCENTE','ESTERNO')),
  fuori_corso BOOLEAN NOT NULL DEFAULT FALSE,
  tessera_id  BIGINT NOT NULL REFERENCES tessere(id) ON DELETE RESTRICT,
  sospeso     BOOLEAN NOT NULL DEFAULT FALSE,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMPTZ NULL
);

CREATE INDEX idx_utenti_tessera ON utenti(tessera_id);

-- =========================
-- PUBBLICAZIONI (base)
-- =========================
CREATE TABLE pubblicazioni (
  id          BIGSERIAL PRIMARY KEY,
  codice      VARCHAR(50) NOT NULL UNIQUE,
  titolo      VARCHAR(200) NOT NULL,
  editore     VARCHAR(200) NOT NULL,
  tipo        VARCHAR(20) NOT NULL CHECK (tipo IN ('LIBRO','RIVISTA')),
  num_copie   INT NOT NULL DEFAULT 0 CHECK (num_copie >= 0),
  prezzo_base NUMERIC(10,2) NOT NULL DEFAULT 0.00 CHECK (prezzo_base >= 0),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMPTZ NULL
);

CREATE INDEX idx_pubblicazioni_tipo ON pubblicazioni(tipo);

-- =========================
-- RIVISTE (dati specifici)
-- =========================
CREATE TABLE riviste (
  pubblicazione_id BIGINT PRIMARY KEY REFERENCES pubblicazioni(id) ON DELETE CASCADE,
  usura            INT NOT NULL DEFAULT 0 CHECK (usura BETWEEN 0 AND 100)
);

-- =========================
-- PRESTITI
-- =========================
CREATE TABLE prestiti (
  id               BIGSERIAL PRIMARY KEY,
  utente_id        BIGINT NOT NULL REFERENCES utenti(id) ON DELETE RESTRICT,
  pubblicazione_id BIGINT NOT NULL REFERENCES pubblicazioni(id) ON DELETE RESTRICT,
  data_inizio      DATE NOT NULL,
  data_fine        DATE NULL,
  aperto           BOOLEAN NOT NULL DEFAULT TRUE,
  prezzo_finale    NUMERIC(10,2) NULL CHECK (prezzo_finale IS NULL OR prezzo_finale >= 0),
  note             VARCHAR(500) NULL,
  created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at       TIMESTAMPTZ NULL
);

CREATE INDEX idx_prestiti_utente ON prestiti(utente_id);
CREATE INDEX idx_prestiti_pubblicazione ON prestiti(pubblicazione_id);
CREATE INDEX idx_prestiti_aperti ON prestiti(aperto);

-- Un utente non può avere due prestiti "aperti" per la stessa pubblicazione
CREATE UNIQUE INDEX uk_prestito_aperto
  ON prestiti (utente_id, pubblicazione_id)
  WHERE aperto = TRUE; 