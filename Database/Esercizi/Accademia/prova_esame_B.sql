-- QUERY 1 
SELECT p.cognome
FROM persona AS p
WHERE p.stipendio <= 40000
;

-- QUERY 2
SELECT DISTINCT p.id, p.nome, p.cognome
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id
WHERE p.stipendio <= 40000
;

-- QUERY 3
SELECT sum(pr.budget)
FROM progetto AS pr
;

-- QUERY 4
SELECT p.nome, p.cognome, sum(pr.budget)
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id
GROUP BY p.id
;

-- QUERY 5
SELECT p.nome, p.cognome, count(pr.id)
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id
WHERE p.posizione = 'Professore Ordinario'
GROUP BY p.id
;

-- QUERY 6
SELECT p.nome, p.cognome, count(ass.id) num_malattie
FROM persona AS p
    JOIN assenza AS ass ON p.id = ass.persona
WHERE p.posizione = 'Professore Associato' AND ass.tipo = 'Malattia'
GROUP BY p.id
;

-- QUERY 7
SELECT p.nome, p.cognome, sum(ap.oreDurata) tot_ore
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id AND pr.id = 5
GROUP BY p.id
;

-- QUERY 8
SELECT p.nome, p.cognome, avg(ap.oreDurata) media_ore
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
GROUP BY p.id
;

-- QUERY 9
SELECT p.nome, p.cognome, sum(anp.oreDurata) tot_ore
FROM persona AS p
    JOIN AttivitaNonProgettuale anp ON p.id = anp.persona
WHERE anp.tipo = 'Didattica'
GROUP BY p.id
;

-- QUERY 10
SELECT sum(ap.oreDurata) tot_ore
FROM persona AS p
    JOIN AttivitaProgetto AS ap ON p.id = ap.persona
    JOIN Progetto AS pr ON ap.progetto = pr.id AND pr.id = 3
    JOIN WP ON wp.progetto = pr.id AND wp.id = 5
GROUP BY p.id
;