begin transaction;
set constraints all deferred;

create table Nazione (
    nome Stringa primary key
);

create table Regione (
    nome Stringa,

    nazione Stringa,
    foreign key (nazione) references Nazione(nome),
    primary key (nome, nazione)
);

create table Citta (
    nome Stringa,

    regione Stringa,
    nazione Stringa,
    foreign key (regione, nazione) references Regione(nome, nazione),
    primary key (nome, regione, nazione)
);

create table Direttore (
    nome Stringa not null,
    cognome Stringa not null,
    cf CodiceFiscale primary key,
    data_nascita date not null,
    anni_servizio IntGEZ not null,

    citta_nasc Stringa not null,
    regione_nasc Stringa not null,
    nazione_nasc Stringa not null,
    foreign key (citta_nasc, regione_nasc, nazione_nasc) references Citta(nome, regione, nazione)
);

create table Dipartimento (
    nome Stringa primary key,
    indirizzo Indirizzo not null,

    direttore CodiceFiscale not null,
    foreign key (direttore) references Direttore(cf)
);


create table Fornitore (
    ragione_sociale Stringa not null,
    partita_iva PartitaIva primary key,
    indirizzo Indirizzo not null,
    telefono Telefono not null,
    email Email not null
);

create table Ordine (
    id integer primary key,
    data_stipula date not null,
    imponibile RealGEZ not null,
    aliquotaIVA Real_0_1 not null,
    descrizione Stringa not null,
    stato Stato not null,

    fornitore PartitaIva not null,
    dipartimento Stringa not null,
    foreign key (fornitore) references fornitore(partita_iva),
    foreign key (dipartimento) references Dipartimento(nome)
);
commit;