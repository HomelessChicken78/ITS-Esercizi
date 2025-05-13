/*Esercizio 1.4
Creare un progetto Javascript che dichiara una
variabile di tipo stringa con valore ‘50’, stampare
a video il valore ed il tipo. Verificare tramite una
funzione globale se il valore è di tipo numerico
oppure no e stampare a video l’esito (true o
false).
Successivamente convertire la stringa in un
numero e stampare a video il valore con il tipo
(che ora è cambiato) */

let s1 = "50"

console.log(s1, typeof(s1))
console.log(typeof(s1) === 'number')

s1 = parseInt(s1)
console.log(s1, typeof(s1))
console.log(typeof(s1) === 'number')