begin transaction;
create table Categoria (
    nome stringa primary key,
    super stringa,

    check (nome <> super)
);

alter table Categoria
add constraint fk_categoria_super
foreign key (super) references categoria(nome);

create table Utente (
    username stringa primary key,
    registrazione timestamp not null
);

-- Da modellare disjoint e complete
create table VenditoreProfessionale (
    vetrina URL not null,
    unique (vetrina),

    isa_ut stringa primary key,
    foreign key (isa_ut) references Utente(username)
);

create table Privato (
    isa_ut stringa primary key,
    foreign key (isa_ut) references Utente(username)
);

create table MetodoDiPagamento (
    nome stringa primary key
);

create table PostOggetto (
    id serial primary key,
    descrizione stringa not null,
    pubblicazione timestamp not null,
    ha_feedback boolean not null,
    voto Voto,
    commento stringa,
    istante_feedback timestamp,

    utente stringa not null,
    foreign key (utente) references utente(username),

    -- v.inclusione (id) occorre in met_post(post),

    categoria stringa not null,
    foreign key (categoria) references Categoria(nome),

    check (istante_feedback is null or istante_feedback > pubblicazione)
    check ( (ha_feedback = True and voto is not null and istante_feedback is not null) or (ha_feedback = False and voto is null and commento is null and istante_feedback is null) )
);

create table met_post (
    metodo stringa,
    post integer,

    primary key (metodo, post),
    foreign key (metodo) references MetodoDiPagamento(nome),
    foreign key (post) references PostOggetto(id)
);

-- Da modellare disjoint e complete
create table PostOggettoNuovo (
    anni_garanzia IntG1 not null,

    isa_po integer primary key,
    foreign key (isa_po) references PostOggetto(id),

    -- Manca vincolo esterno
    venditore stringa not null,
    foreign key (venditore) references VenditoreProfessionale(isa_ut)
);

create table PostOggettoUsato (
    anni_garanzia IntGEZ not null,
    condizione Condizione not null,

    isa_po integer primary key,
    foreign key (isa_po) references PostOggetto(id)
);

-- Da modellare disjoint e complete
create table Asta (
    prezzo_base RealGEZ not null,
    prezzo_bid RealGZ not null,
    scadenza timestamp not null,

    isa_po integer primary key,
    foreign key (isa_po) references PostOggetto(id)
);


create table CompraloSubito (
    prezzo RealGZ not null,

    isa_po integer primary key,
    foreign key (isa_po) references PostOggetto(id),

    acquirente stringa,
    foreign key (acquirente) references Privato(isa_ut),

    istante_acquisto timestamp,
    check ( (istante_acquisto is null and acquirente is null) or (istante_acquisto is not null and acquirente is not null) )
);

create table Bid (
    codice serial primary key,
    istante timestamp not null,

    asta integer not null,
    foreign key (asta) references Asta(isa_po),

    unique (istante, asta),

    privato stringa not null,
    foreign key (privato) references Privato(isa_ut)
);

commit;
