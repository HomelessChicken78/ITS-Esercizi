begin transaction;

set contraints all deferred;

CREATE DOMAIN Stringa as varchar;

CREATE DOMAIN IntGZ as Integer
    check (value > 0);

CREATE DOMAIN Real_0_10 as real
    check (value >= 0 and value <= 8);

CREATE TYPE regole as ENUM
('Giapponesi', 'Cinesi');

CREATE TYPE colore as ENUM
('Bianco', 'Nero');

CREATE TYPE indirzzo as (
    via Stringa,
    civico Stringa
);

create table nazione (
    nome stringa primary key
);

create table regione (
    nome stringa not null,
    nazione stringa not null,
    primary key (nome, nazione),

    foreign key (nazione) references nazione(nome)
);

create table citta (
    id integer primary key
    nome stringa not null,
    regione stringa not null,
    nazione stringa not null,

    unique (nome, regione, nazione),

    foreign key (regione, nazione)
        references regione(nome, regione, nazione)
);

create table giocatore (
    nickname stringa primary key,
    nome stringa not null,
    cognome stringa not null,
    indirizzo indirizzo not null,
    rank IntGZ not null,
    citta integer not null,

    foreign key (citta) references citta(id)
);

create table torneo (
    id integer primary key,
    nome stringa not null,
    descrizione stringa not null,
    anno_edizione integer not null
);

create table partita (
    id integer primary key,
    data date not null,
    regole regole not null,
    indirizzo indirizzo not null,
    komi Real_0_10 not null,

    -- accorpo l'associazione bianco
    bianco stringa not null,
    foreign key (bianco)
        references giocatore(nickname) deferrable,

    -- non accorpo l'associazione nero
    -- v. incl. id appare in nero(partita)

    torneo integer, -- può essere null, è [0..1]
    foreign key (torneo)
        references torneo(id),
);

create table nero (
    giocatore stringa not null,
    partita integer not null,
    primary key (partita), -- una partita ha un solo giocatore
    foreign key (giocatore)
        references giocatore(nickname),
    foreign key (partita)
        references partita(id)
);

create table PartitaConPunteggi (
    -- devo necessariamente accorpare punt_isa_part perchè ospita l'identificatore prima
    partita integer primary key,

    foreign key (partita) references partita(id),
    punteggio_bianco IntGZ not null,
    punteggio_nero IntGZ not null,

    foreign key (partita) references partita(id),
    rinunciatario colore not null
);

alter table partita add constraint partita_nero_fk
    foreign key (id) references nero(partita) deferrable;

commit;

-- begin transaction;

-- set constraint all deferred;

-- insert into giocatore (...) values ("me", ...);
-- insert into partita ...
-- insert into nero ...
-- commit;