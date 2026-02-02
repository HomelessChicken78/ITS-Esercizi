BEGIN TRANSACTION;

CREATE DOMAIN intGE1800 AS integer
    CHECK (value > 1900);

CREATE TABLE Utente (
    nome varchar not null,
    cognome varchar not null,
    username varchar primary key,
    password varchar not null,
    annoNascita intGE1800 not null
);

COMMIT;