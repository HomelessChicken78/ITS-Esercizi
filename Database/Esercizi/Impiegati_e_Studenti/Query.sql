-- 1. Quali sono i nomi degli impiegati nati a partire dall'anno 

select nome
from persona, impiegato
where persona.cf = impiegato.persona
order by data_nascita asc

-- 2. Quali sono i nomi di tutti i progetti?

select nome
from progetto

-- 3. Quali sono gli stipendi dei direttori?

select stipendio
from impiegato
where ruolo = 'Direttore'

-- 4. Quanti sono i progettisti?

select count(*)
from impiegato
where ruolo = 'Progettista'

-- 5 Quanti sono i responsabili?

select count(*)
from impiegato, progetto
where progetto.resp_prog = impiegato.persona


-- 7. Qual è lo stipendio medio dei segretari?

select avg(stipendio)
from impiegato
where ruolo = 'Segretario'

-- 8. Qual è l'età della/o studente meno giovane?
-- usare select(date_part('year',age(current_date, <DATA DI NASCITA>))) as eta FROM [...];

select max((date_part('year',age(current_date, data_nascita)))) as eta
from persona, studente
where persona.cf = studente.persona

-- 9. Quanti sono i direttori che hanno assolto agli obblighi militari?

select count(*)
from impiegato, persona
where impiegato.ruolo = 'Direttore' and persona.cf = impiegato.persona and persona.pos_uomo is not null

-- 10. Quanti sono i progetti di cui è responsabile un'impiegata con almeno due figli?

select count(*)
from progetto, persona
where progetto.resp_prog = persona.cf and persona.maternita >= 2