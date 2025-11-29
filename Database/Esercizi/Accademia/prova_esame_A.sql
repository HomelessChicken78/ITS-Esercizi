-- QUERY 1
-- Elencare tutti i progetti la cui fine è successiva al
-- 2023-12-31.
SELECT pr.nome
FROM progetto AS pr
WHERE pr.fine > '2023-12-31'
;

-- QUERY 2
-- Contare il numero totale di persone per ciascuna posizione
-- (Ricercatore, Professore Associato, Professore Ordinario)
SELECT p.posizione, count(*)
FROM persona AS p
GROUP BY p.posizione
;

-- QUERY 3
-- Restituire gli id e i nomi delle persone che hanno almeno
-- un giorno di assenza per "Malattia"
SELECT DISTINCT p.id, p.nome
FROM persona AS p
    JOIN assenza AS ass ON p.id = ass.persona
WHERE ass.tipo = 'Malattia'
;

-- QUERY 4
-- Per ogni tipo di assenza, restituire il numero complessivo
-- di occorrenze
SELECT ass.tipo, count(*) numero_occorrenze
FROM assenza AS ass
GROUP BY ass.tipo
;

-- QUERY 5
-- Calcolare lo stipendio massimo tra tutti i "Professori
-- Ordinari".
SELECT max(p.stipendio) stipendio_piu_alto
FROM persona AS p
WHERE p.posizione = 'Professore Ordinario'
;

-- QUERY 6
--Quali sono le attività e le ore spese dalla persona con id 1
-- nelle attività del progetto con id 4, ordinate in ordine
-- decrescente. Per ogni attività, restituire l’id, il tipo e il
-- numero di ore
SELECT  ap.id, ap.tipo, ap.oreDurata
FROM attivitaprogetto AS ap
WHERE ap.persona = 1 AND ap.progetto = 4
ORDER BY ap.id DESC
;

-- QUERY 7
-- Quanti sono i giorni di assenza per tipo e per persona. Per
-- ogni persona e tipo di assenza, restituire nome, cognome,
-- tipo assenza e giorni totali.
SELECT p.nome, p.cognome, ass.tipo, count(*) giorni_totali
FROM persona AS p
    JOIN assenza AS ass ON p.id = ass.persona
GROUP BY p.id, p.nome, p.cognome, ass.tipo
;

-- QUERY 8
-- Restituire tutti i “Professori Ordinari” che hanno lo
-- stipendio massimo. Per ognuno, restituire id, nome e
-- cognome
WITH d AS (
    SELECT max(p.stipendio) maxim
    FROM persona AS p
    WHERE p.posizione = 'Professore Ordinario'
)

SELECT p.id, p.nome, p.cognome
FROM persona AS p, d
WHERE p.posizione = 'Professore Ordinario' AND p.stipendio = d.maxim
;

-- QUERY 9
-- Restituire la somma totale delle ore relative alle attività
-- progettuali svolte dalla persona con id = 3 e con durata
-- minore o uguale a 3 ore.
SELECT sum(ap.oreDurata)
FROM attivitaprogetto AS ap
WHERE ap.oreDurata <= 3 AND ap.persona = 3
;

-- QUERY 10
-- Restituire gli id e i nomi delle persone che non hanno
-- mai avuto assenze di tipo "Chiusura Universitaria"
SELECT p.id, p.nome
FROM persona AS p
    LEFT JOIN assenza AS ass ON p.id = ass.persona and ass.tipo = 'Chiusura Universitaria'
WHERE ass.id IS NULL
;