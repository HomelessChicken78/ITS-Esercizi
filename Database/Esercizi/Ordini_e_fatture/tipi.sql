begin transaction;
set constraints all deferred;

create domain stringa as varchar;

create domain IntGEZ as integer
    check (value >= 0);

create domain RealGEZ as real
    check (value >= 0);

create domain Real_0_1 as real
    check (value >= 0 and value <= 1);

create type Stato as enum (
    'in preparazione',
    'inviato',
    'da saldare',
    'saldato'
);

create type Indirizzo as (
    via Stringa,
    civico Stringa,
    CAP char(5)
);

create domain CodiceFiscale as Stringa
    check (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

create domain PartitaIva as Stringa
    check (value ~ '^[0-9]{11}$');

create domain Telefono as Stringa
    check (value ~ '^\+[1-9][0-9]{0,2} [0-9]{6,13}$');

create domain Email as Stringa
    check (value ~ '^[\w\.-]+@[\w\.-]+\.\w{2,}$');

commit;