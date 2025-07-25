-- 1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?

select codice, comp
from volo
where durataminuti > 180;

-- 2. Quali sono le compagnie che hanno voli che superano le 3 ore?

select distinct nome
from compagnia comp, volo v
where comp.nome = v.comp
and durataminuti > 180;

-- 3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con
-- codice ‘CIA’?

select distinct v.codice, part.comp
from volo v, arrpart part, aeroporto aero
where v.codice = part.codice and v.comp = part.comp
and part.partenza = aero.codice
and aero.codice = 'CIA';

-- 4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice
-- ‘FCO’?

select distinct v.comp
from volo v, arrpart arr
where v.codice = arr.codice and v.comp = arr.comp
and arr.arrivo = 'FCO';

-- 5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
-- e arrivano all’aeroporto ‘JFK’ ?

select distinct v.codice, v.comp
from volo v, arrpart ap
where v.codice = ap.codice and v.comp = ap.comp
and ap.partenza = 'FCO' and ap.arrivo = 'JFK';

-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atter-
-- rano all’aeroporto ‘JFK’ ?

select distinct v.comp
from volo v, arrpart ap
where v.codice = ap.codice and v.comp = ap.comp
and ap.partenza = 'FCO' and ap.arrivo = 'JFK';

-- 7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla
-- città di ‘New York’ ?

select distinct v.comp
from volo v, arrpart ap, luogoaeroporto citta, luogoaeroporto citta2
where v.codice = ap.codice and v.comp = ap.comp
and ap.partenza = citta.aeroporto and citta.citta = 'Roma'
and ap.arrivo = citta2.aeroporto and citta2.citta = 'New York';

-- 8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
-- della compagnia di nome ‘MagicFly’ ?

select distinct aero.codice, aero.nome, luogo.citta
from volo v, arrpart part, aeroporto aero, luogoaeroporto luogo
where v.comp = 'MagicFly'
and v.codice = part.codice and v.comp = part.comp
and part.partenza = aero.codice
and aero.codice = luogo.aeroporto;

-- 9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
-- atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice
-- del volo, nome della compagnia, e aeroporti di partenza e arrivo.

select v.codice, v.comp, ap.partenza, ap.arrivo
from volo v, arrpart ap, luogoaeroporto citta, luogoaeroporto citta2
where v.codice = ap.codice and v.comp = ap.comp
and ap.partenza = citta.aeroporto and citta.citta = 'Roma'
and ap.arrivo = citta2.aeroporto and citta2.citta = 'New York';

-- 10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
-- voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
-- qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
-- codici dei voli, e aeroporti di partenza, scalo e arrivo

select *
from arrpart ap, arrpart ap2, luogoaeroporto luogo, luogoaeroporto luogo2
where ap.arrivo = ap2.partenza
and ap.comp = ap2.comp
and ap.partenza = luogo.aeroporto and luogo.citta = 'Roma'
and ap2.arrivo = luogo2.aeroporto and luogo2.citta = 'New York';

-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atter-
-- rano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?

select distinct c.nome
from compagnia c, arrpart ap
where ap.partenza = 'FCO' and ap.arrivo = 'JFK'
and ap.comp = c.nome
and c.annofondaz is not null