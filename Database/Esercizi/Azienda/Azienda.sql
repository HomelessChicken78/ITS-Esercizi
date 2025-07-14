begin transaction;
set constraints all deferred;

create domain RealGEZ as integer
    check (value >= 0);

create domain Stringa as varchar;

create type Denaro as (
    valore RealGEZ,
    valuta varchar(3)
);

create type Indirizzo as (
    via Stringa,
    civico Stringa,
    CAP varchar(5)
);

create table Progetto (
    id integer primary key,
    nome stringa not null,
    budget Denaro not null
);

create table Impiegato (
    id integer primary key,
    nome stringa not null,
    cognome stringa not null,
    data_nascita date not null,
    stipendio denaro not null

    -- v.incl. Impiegato(id) occorre in afferisce(impiegato)
);

create table partecipa (
    impiegato integer not null,
    progetto integer not null,

    primary key (impiegato, progetto),

    foreign key (impiegato) references impiegato(id),
    foreign key (progetto) references progetto(id)
);

create table Dipartimento (
    id integer primary key,
    nome stringa not null,
    telefono stringa not null
);

create table afferisce (
    impiegato integer primary key,
    dipartimento integer not null,
    data_afferenza date not null,

    foreign key (impiegato) references impiegato(id),
    foreign key (dipartimento) references dipartimento(id)
);

create table dirige (
    impiegato integer not null,
    dipartimento integer primary key,

    foreign key (impiegato) references impiegato(id),
    foreign key (dipartimento) references dipartimento(id)
);
commit;