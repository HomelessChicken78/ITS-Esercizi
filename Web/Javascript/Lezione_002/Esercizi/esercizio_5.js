/*
Esercizio 1.5
Creare un progetto Javascript che memorizza
all’interno di una variabile i giorni della settimana
separati dalla virgola e stampare a video tramite
console.log() il risultato. Scrivere il codice in modo
che, facendo la modifica ad un solo valore, i giorni
della settimana vengono visualizzati uno sotto
l’altro senza la virgola.
*/

sep = ", ";
giorni = `lunedi'${sep}martedi'${sep}mercoledi'${sep}giovedi'${sep}venerdi'${sep}sabato${sep}domenica`; // prova a modificare questa stringa e vedi che succede
console.log(giorni);

if (giorni === "lunedi', martedi', mercoledi', giovedi', venerdi', sabato, domenica"){
    console.log(giorni);
}else{
    sep = "\n";
    console.log(`lunedi'${sep}martedi'${sep}mercoledi'${sep}giovedi'${sep}venerdi'${sep}sabato${sep}domenica`);
}