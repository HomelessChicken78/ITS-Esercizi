-- QUERY 1 
--Quali sono le persone con stipendio di al massimo 40000
-- euro
SELECT p.cognome
FROM persona AS p
WHERE p.stipendio <= 40000
;

-- QUERY 2
-- Quali sono i ricercatori che lavorano ad almeno un
-- progetto e hanno uno stipendio di al massimo 40000
SELECT DISTINCT p.id, p.nome, p.cognome
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id
WHERE p.stipendio <= 40000
;

-- QUERY 3
-- Qual è il budget totale dei progetti nel db
SELECT sum(pr.budget)
FROM progetto AS pr
;

-- QUERY 4
-- Qual è il budget totale dei progetti a cui lavora ogni
-- persona. Per ogni persona restituire nome, cognome e
-- budget totale dei progetti nei quali è coinvolto
SELECT p.nome, p.cognome, sum(pr.budget)
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id
GROUP BY p.id
;

-- QUERY 5
-- Qual è il numero di progetti a cui partecipa ogni
-- professore ordinario. Per ogni professore ordinario,
-- restituire nome, cognome, numero di progetti nei quali è
-- coinvolto
SELECT p.nome, p.cognome, count(DISTINCT pr.id)
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id
WHERE p.posizione = 'Professore Ordinario'
GROUP BY p.id
; -- !!! : NON C'ERA IL DISTINCT

-- QUERY 6
-- Qual è il numero di assenze per malattia di ogni
-- professore associato. Per ogni professore associato,
-- restituire nume, cognome e numero di assenze per
-- malattia
SELECT p.nome, p.cognome, count(ass.id) num_malattie
FROM persona AS p
    JOIN assenza AS ass ON p.id = ass.persona
WHERE p.posizione = 'Professore Associato' AND ass.tipo = 'Malattia'
GROUP BY p.id
;

-- QUERY 7
-- Qual è il numero totale di ore, per ogni persona, dedicate
-- al progetto con id ‘5’. Per ogni persona che lavora al
-- progetto, restituire nome, cognome e numero di ore totali
-- dedicate ad attività progettuali relative al progetto
SELECT p.nome, p.cognome, sum(ap.oreDurata) tot_ore
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id AND pr.id = 5
GROUP BY p.id
;

-- QUERY 8
-- Qual è il numero medio di ore delle attività progettuali
-- svolte da ogni persona. Per ogni persona, restituire nome,
-- cognome e numero medio di ore delle sue attività
-- progettuali (in qualsivoglia progetto
SELECT p.nome, p.cognome, avg(ap.oreDurata) media_ore
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
GROUP BY p.id
;

-- QUERY 9
-- Qual è il numero totale di ore, per ogni persona, dedicate
-- alla didattica. Per ogni persona che ha svolto attività
-- didattica, restituire nome, cognome e numero di ore totali
-- dedicate alla didattica
SELECT p.nome, p.cognome, sum(anp.oreDurata) tot_ore
FROM persona AS p
    JOIN AttivitaNonProgettuale anp ON p.id = anp.persona
WHERE anp.tipo = 'Didattica'
GROUP BY p.id
;

-- QUERY 10
-- Quali sono le persone che hanno svolto attività nel WP
-- di id ‘5’ del progetto con id ‘3’. Per ogni persona, restituire
-- il numero totale di ore svolte in attività progettuali per il
-- WP in questione
SELECT sum(ap.oreDurata) tot_ore
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id AND pr.id = 3
    JOIN WP ON wp.progetto = pr.id AND wp.id = 5
GROUP BY p.id