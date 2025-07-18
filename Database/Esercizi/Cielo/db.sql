begin transaction;
set constraints all deferred;

create domain posinteger as integer
    check (value >= 0);

create domain StringaM as varchar(100);

create domain CodIATA as char(3);

create table Compagnia (
    nome StringaM primary key,
    annoFondaz PosInteger -- Null perchè è [0..1]
);

create table LuogoAeroporto (
    aeroporto CodIATA primary key,
    citta StringaM not null,
    nazione StringaM not null

    -- fk aggiunta dopo
);

create table Aeroporto (
    codice CodIATA primary key,
    nome StringaM not null,

    foreign key (codice) references LuogoAeroporto(aeroporto) deferrable
);

alter table LuogoAeroporto add constraint luogo_aerop_fk
    foreign key (aeroporto) references Aeroporto(codice) deferrable;

create table Volo (
    codice PosInteger not null,
    comp StringaM not null,
    durataMinuti PosInteger not null,

    primary key (codice, comp),

    foreign key (comp) references Compagnia(nome) deferrable
    -- fk aggiunta dopo
);

create table ArrPart (
    codice PosInteger not null,
    comp StringaM not null,
    arrivo CodIATA not null,
    partenza CodIATA not null,

    primary key (codice, comp),
    foreign key (codice, comp) references Volo(codice, comp) deferrable,
    foreign key (arrivo) references Aeroporto(codice),
    foreign key (partenza) references Aeroporto(codice)
);

alter table Volo add constraint volo_arrpart_fk
    foreign key (codice, comp) references ArrPart(codice, comp) deferrable;

commit;