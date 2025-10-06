-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi
-- aeroporti?
select ae.codice, ae.nome, count(distinct ap.comp)
from aeroporto ae, arrpart ap
where ae.codice = ap.arrivo or ae.codice = ap.partenza
group by ae.codice;

-- 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno
-- 100 minuti?
select count(*)
from arrpart part, volo v
where part.partenza = 'HTR' 
and part.codice = v.codice
and v.durataminuti > 100;


-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
-- nella quale opera?
select nazione, count(distinct aeroporto)
from arrpart ap, luogoaeroporto l
where ap.comp = 'Apitalia' and (ap.arrivo = l.aeroporto or ap.partenza = l.aeroporto)
group by nazione;


-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
-- compagnia ‘MagicFly’ ?
select round(avg(durataminuti), 2) media, max(durataminuti) massimo, min(durataminuti) minimo
from volo v
where v.comp = 'MagicFly';


-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
-- aeroporti?
-- Per ogni aeroporto voglio sapere tutte le compagnie che ci operano. Di queste voglio sapere la piu vecchia
select ae.codice, ae.nome, min(annofondaz)
from arrpart ap, compagnia c, aeroporto ae
where ap.comp = c.nome
and (ap.arrivo = ae.codice or ap.partenza  = ae.codice)
group by ae.codice, ae.nome;


-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più
-- voli?
-- dato una nazione di partenza, raggruppa le nazioni che questa può raggiungere tramite i voli disponibili.
-- Per ogni gruppo, quante sono le nazioni raggiungibili?
-- Note: aereporto di partenza e di arrivo devono essere diversi. Ma non basta.§
-- Infatti ci possono essere più aeroporti nella stessa nazione. E contare quello non sarebbe corretto
select l_part.nazione, count(distinct l_arr.nazione)
from luogoaeroporto l_part, luogoaeroporto l_arr, arrpart ap
where l_part.nazione <> l_arr.nazione
and ap.partenza = l_part.aeroporto and ap.arrivo = l_arr.aeroporto
group by l_part.nazione;

-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?
-- Per ogni aereporto, determinare i suoi voli in partenza. Dopodichè fare la media della durata per ogni gruppo.
select ae.codice, ae.nome, round(avg(durataminuti), 2)
from aeroporto ae, arrpart part, volo v
where part.partenza = ae.codice and v.codice = part.codice and v.comp = part.comp
group by ae.codice, ae.nome;

-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
-- a partire dal 1950?
-- Date solo le compagnie fondate dopo il 1950, prendere i voli di tali compagnie e farne la somma della durata di tutti i voli
select c.nome, sum(durataminuti) totale_durate
from compagnia c, arrpart ap, volo v
where c.annofondaz >= 1950
and ap.comp = c.nome and ap.codice = v.codice and ap.comp = v.comp
group by c.nome;


-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?
-- Presi tutti gli aeroporti, conta le compagnie che vi hanno voli in partenza o in arrivo.
-- Se il loro numero è esattamente 2, visualizzale
select ae.codice, ae.nome
from aeroporto ae, arrpart ap
where (ae.codice = ap.arrivo or ae.codice = ap.partenza)
group by ae.codice, ae.nome
having count(distinct ap.comp) = 2;

-- 10. Quali sono le città con almeno due aeroporti?
select l.citta
from luogoaeroporto l
group by l.citta
having count(l.aeroporto) >= 2;


-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6
-- ore?
-- Prendi tutti i voli e associali a una compagnia. Raggruppa i voli a seconda della compagnia e fanne la media.
-- Se la media è > 6, visualizzala
select c.nome compagnia, round(avg(durataminuti), 1) media
from volo v, compagnia c
where v.comp = c.nome
group by c.nome
having avg(durataminuti) > 360;

-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100
-- minuti?
-- Associa ogni volo ad una compagnia. Raggruppa per compagnia
-- se il valore piu basso per la durata è > 100 allora tutti i valori per quel gruppo sono > 100
select c.nome compagnia
from volo v, compagnia c
where v.comp = c.nome
group by c.nome
having min(v.durataminuti) > 100;

--13. Qual'è il nome delle compagnie che hanno il volo più lungo?


WITH D AS(

    SELECT MAX(durataMinuti) AS massimaDurata
    FROM Volo
)

--D è una tabella 1x1 con una sola colonna 'max_durata'

SELECT DISTINCT v.comp
FROM Volo,D 
-- Risulta in una tavella in cui ogni ennupla è una ennupla di 'volo' con  anche il valore 'D.massimaDurata'


-- In maniera alternativa
SELECT comp
FROM Volo v, D 
GROUP BY comp, D.massimaDurata
HAVING MAX(durataMinuti) > D.massimaDurata

--14. Qual'è il nome delle compagnie che non hanno voli ?