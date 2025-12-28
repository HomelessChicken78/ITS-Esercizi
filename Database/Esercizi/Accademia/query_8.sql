-- 1. Quali sono le persone (id, nome e cognome) che hanno avuto assenze solo nei
-- giorni in cui non avevano alcuna attivitÃ (progettuali o non progettuali)

select *
from persona p
	left join assenza a on p.id = a.persona
	left join attivitaprogetto ap on (p.id = ap.persona and ap.giorno = a.giorno)
	left join attivitanonprogettuale anp on (p.id = anp.persona and anp.giorno = a.giorno)
where ap.id is null and anp.id is null
order by p.id

-- 1. Quali sono le persone (id, nome e cognome) che hanno avuto assenze solo nei
-- giorni in cui non avevano alcuna attivitÃ (progettuali o non progettuali)

select p.id, p.nome, p.cognome,
a.id id_assenza, a.tipo tipo_assenza, a.giorno giorno_assenza,
ap.id id_attivita_p, ap.tipo tipo_attivita_p, ap.giorno giorno_attivita_p,
anp.id id_attivita_np, anp.giorno giorno_attivita_np
from persona p
	left join assenza a on p.id = a.persona
	left join attivitaprogetto ap on (p.id = ap.persona and ap.giorno = a.giorno)
	left join attivitanonprogettuale anp on (p.id = anp.persona and anp.giorno = a.giorno)
where ap.id is null and anp.id is null
order by p.id


-- 2. Quali sono le persone (id, nome e cognome) che non hanno mai partecipato ad
-- alcun progetto durante la durata del progetto “Pegasus”

-- 3. Quali sono id, nome, cognome e stipendio dei ricercatori con stipendio maggiore
-- di tutti i professori (associati e ordinari)?