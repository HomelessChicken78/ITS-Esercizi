create database esami;
\c esami

create domain posint as integer
    check (value > 0);

create domain posint_not_null as posint
    check (value is not null);

create domain string_not_null as varchar(255)
    check (value is not null);

create type indirizzo as (
    via string_not_null,
    cap char(5),
    civico posint_not_null
);

create sequence docente_mat_seq;

create table docente (
    mat integer primary key,
    nome varchar(100) not null,
    cognome varchar(100) not null,
    email varchar(100) not null
);

create table corso (
    codice integer primary key,
    nome varchar not null,
    aula varchar(2) not null
);

create table incarico (
    docente integer not null,
    corso integer not null,
    primary key(docente, corso),
    foreign key (docente) references docente(mat),
    foreign key (corso) references corso(codice)
);

alter table docente alter column mat set default nextval('docente_mat_seq');