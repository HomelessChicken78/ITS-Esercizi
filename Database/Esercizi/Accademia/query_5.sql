-- Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome
-- ‘Pegasus’ 

select wp.nome, wp.inizio, wp.fine
from wp, progetto pr
where wp.progetto = pr.id
and pr.nome = 'Pegasus'

-- Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
-- una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?

select distinct p.nome, p.cognome, p.posizione, pr.nome
from persona p, attivitaprogetto ap, progetto pr
where p.id = ap.persona and ap.progetto = pr.id and pr.nome = 'Pegasus'
order by cognome desc

-- Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
-- una attività nel progetto ‘Pegasus’ ?

select distinct p.nome, p.cognome, p.posizione
from persona as p, attivitaprogetto as ap, attivitaprogetto as ap2,progetto as pr
where p.id = ap.persona and ap.progetto = pr.id and pr.nome ='Pegasus'
and ap2.id <> ap.id and ap2.persona = ap.persona
and ap2.progetto = ap.progetto
order by p.cognome desc

-- Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto almeno una assenza per malattia?

select distinct nome, cognome, posizione
from persona p, assenza a
where p.posizione = 'Professore Ordinario'
and p.id = a.persona
and a.tipo = 'Malattia'

-- Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto più di una assenza per malattia?

select distinct nome, cognome, posizione
from persona p, assenza a, assenza a2
where p.posizione = 'Professore Ordinario'
and p.id = a.persona and p.id = a2.persona
and a.tipo = 'Malattia'
and a.id <> a2.id

-- Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
-- un impegno per didattica?

select distinct nome, cognome, posizione
from persona p, attivitanonprogettuale anp
where p.posizione = 'Ricercatore' and anp.tipo = 'Didattica'
and anp.persona = p.id

-- Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
-- impegno per didattica?

select distinct nome, cognome, posizione
from persona p, attivitanonprogettuale anp, attivitanonprogettuale anp2
where p.id = anp.persona and p.id = anp2.persona
and p.posizione = 'Ricercatore'
and anp.tipo = 'Didattica'
and anp.id <> anp2.id

-- Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali?

select distinct p.nome, p.cognome
from persona p, attivitaprogetto ap, attivitanonprogettuale anp
where p.id = ap.persona and p.id = anp.persona
and ap.giorno = anp.giorno

-- Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali? Si richiede anche di proiettare il
-- giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
-- entrambe le attività?

select distinct p.nome, p.cognome, ap.giorno, pr.nome prj, ap.oredurata h_prj, anp.tipo att_noprj, anp.oredurata h_noprj
from persona p, attivitaprogetto ap, attivitanonprogettuale anp, progetto pr
where p.id = ap.persona and p.id = anp.persona
and ap.giorno = anp.giorno
and pr.id = ap.progetto

-- Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali?

select distinct p.nome, cognome
from persona p, assenza a, attivitaprogetto ap
where a.persona = p.id and ap.persona = p.id
and ap.giorno = a.giorno

-- Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
-- nome del progetto, la causa di assenza e la durata in ore della attività progettuale?

select distinct p.nome, cognome, a.giorno, a.tipo causa_ass, pr.nome progetto, ap.oredurata ore_att_prj
from persona p, assenza a, attivitaprogetto ap, progetto pr
where a.persona = p.id and ap.persona = p.id
and ap.giorno = a.giorno
and ap.progetto = pr.id

-- Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?

select distinct wp.nome
from wp wp, wp wp2
where wp.progetto <> wp2.progetto
and wp.nome = wp2.nome