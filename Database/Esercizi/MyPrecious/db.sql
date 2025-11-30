CREATE DATABASE MyPrecious;
\c MyPrecious



-- Tipi di dato
BEGIN TRANSACTION;
CREATE DOMAIN Stringa AS varchar;

CREATE  DOMAIN RealGEZ AS real
    CHECK (value >= 0);
COMMIT;



-- Traduzione diretta
BEGIN TRANSACTION;
CREATE TABLE Nazione (
    nome Stringa primary key
);

CREATE TABLE Regione (
    nome Stringa not null,

    nazione Stringa not null,
    foreign key (nazione)
        references Nazione(nome),

    primary key (nome, nazione)
);

CREATE TABLE Citta (
    nome Stringa not null,

    regione Stringa not null,
    nazione Stringa not null,
    foreign key (regione, nazione)
        references Regione(nome, nazione),

    primary key (nome, regione, nazione)
);

CREATE TABLE Artista (
    id serial primary key,
    nome_arte Stringa not null,
    data_nascita date not null,
    data_morte date,

    CHECK ((data_morte is null) or (data_morte > data_nascita))
);

CREATE TABLE Tariffa (
    id serial primary key,
    nome Stringa not null,
    prezzo_base RealGEZ not null
);

CREATE TABLE Biglietto (
    id serial primary key,
    istante_vendita timestamp not null,
    validita date not null,

    CHECK (validita >= istante_vendita), -- istante_vendita è automaticamente convertito in un date

    tariffa integer not null,
    foreign key (tariffa)
        references Tariffa(id)
);

-- N.B.: Il disj e il compl non sono implementati --------------------------------
CREATE TABLE Standard (
    biglietto integer primary key,
    foreign key (biglietto)
        references Biglietto(id)
);

CREATE TABLE ExtendedAccess (
    biglietto integer primary key,
    foreign key (biglietto)
        references Biglietto(id)
    -- v.incl. (biglietto) occorre in ext_temp(extended_access)
);
---------------------------------------------------------------------------------

CREATE TABLE Esposizione (
    id serial primary key,
    nome Stringa not null,
    inizio date not null,
    is_temp boolean not null,
    fine date,
    tema Stringa,
    prezzo_accesso RealGEZ,

    CHECK ((fine is null) or (fine >= inizio)),
    CHECK (
        (is_temp = true and fine is not null and tema is not null and prezzo_accesso is not null)
            or
        (is_temp = false and fine is null and tema is null and prezzo_accesso is null)
    )
    -- N.B.: Manca il controllo che is_temp = true perchè esista il link (ext, esp):ext_temp, dove ext:ExtendedAccess
);

CREATE TABLE ext_temp (
    extended_access integer not null,
    foreign key (extended_access)
        references ExtendedAccess(biglietto),

    esposizione_temporanea integer not null,
    foreign key  (esposizione_temporanea)
        references Esposizione,

    primary key (extended_access, esposizione_temporanea)
);

CREATE TABLE Tecnica (
    nome Stringa primary key
);

CREATE TABLE Categoria (
    nome Stringa primary key
);

CREATE TABLE CorrenteArtistica (
    nome Stringa primary key
);

CREATE TABLE Opera (
    id serial primary key,
    nome Stringa not null,
    anno_realizzazione integer not null,

    artista integer,
    foreign key (artista)
        references Artista(id),
    
    tecnica Stringa,
    foreign key (tecnica)
        references Tecnica(nome),

    categoria Stringa not null,
    foreign key (categoria)
        references Categoria(nome)
    
    -- v.incl. (id) occorre in op_corr(opera)
);

CREATE TABLE op_corr (
    opera integer not null,
    foreign key (opera)
        references Opera(id),

    corrente_artistica Stringa not null,
    foreign key (corrente_artistica)
        references CorrenteArtistica(nome),
    
    primary key (opera, corrente_artistica)
);

CREATE TABLE espone (
    inizio date not null,
    fine date,

    CHECK ((fine is null) or (fine >= inizio)),

    opera integer not null,
    foreign key (opera)
        references Opera(id),

    esposizione integer not null,
    foreign key (esposizione)
        references Esposizione(id),

    primary key (opera, esposizione)
);
COMMIT;