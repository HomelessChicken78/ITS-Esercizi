begin transaction;
create domain stringa as varchar;

create domain url as varchar;

create domain IntG1 as integer
check (value > 1);

create domain IntGEZ as integer
check (value >= 0);

create domain RealGZ as real
check (value > 0);

create domain RealGEZ as real
check (value >= 0);

create domain Voto as integer
check (value >= 1 and value <= 5);

create type condizione as enum (
    'Ottimo', 'Discreto', 'Da Sistemare'
);
commit;