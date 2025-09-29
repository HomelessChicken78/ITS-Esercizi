-- 1. Quanti sono gli strutturati di ogni fascia?
select posizione, count(*) numero
from persona
group by posizione;

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?
select count(*) totale
from persona
where stipendio >= 40000;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?
select count(*) numero
from progetto
where budget >= 50000 and fine <= CURRENT_DATE;

-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’ ?
select avg(oredurata) media, max(oredurata) massimo, min(oredurata) minimo
from attivitaprogetto
where attivitaprogetto.progetto = 1;

-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
--	‘Pegasus’ da ogni singolo docente?
select persona.nome, persona.cognome, round(avg(ap.oredurata), 2) media, max(ap.oredurata) massimo, min(ap.oredurata) minimo
from persona, attivitaprogetto ap
where ap.progetto = 1 and ap.persona = persona.id
group by persona.id;

-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?
select p.nome, p.cognome, sum(anp.oredurata) somma
from attivitanonprogettuale anp, persona p
where anp.tipo = 'Didattica' and anp.persona = p.id
group by p.id;

-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?
select round(avg(stipendio)) media, max(stipendio) massimo, min(stipendio) minimo
from persona
where posizione ='Ricercatore';

-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
--	associati e dei professori ordinari?
select posizione, round(avg(stipendio)) media, max(stipendio) massimo, min(stipendio) minimo
from persona
group by posizione;

-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?
select pr.nome nome_progetto, sum(ap.oredurata) ore
from persona p, attivitaprogetto ap, progetto pr
where p.nome = 'Ginevra' and p.cognome = 'Riva' and p.id = ap.persona and ap.progetto = pr.id
group by pr.id;

-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?
select pr.id, pr.nome
from attivitaprogetto ap, progetto pr
where ap.progetto = pr.id
group by pr.id
having count(distinct ap.persona) > 2;

-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?
select p.id, p.nome, p.cognome
from persona p, attivitaprogetto ap
where p.posizione = 'Professore Associato' and p.id = ap.persona
group by p.id
having count(*) > 1;