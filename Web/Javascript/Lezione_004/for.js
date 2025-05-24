// Un altro caso di iterazione è il for.
// Il for è molto comodo perchè permette modificare automaticamente una variabile a ogni iterazione,
// senza il bisogno di fare un'istruzione esplicita all'interno del ciclo stesso.
// La variabile che verrà automaticamente aumentata ogni iterazione può
// esser definita direttamente all'interno del for
// invece che dichiararla prima come abbiamo fatto per il while

for (let contatore = 0; contatore < 3; contatore++) {
    console.log(contatore);
}
console.log("Finito!\n");

// Abbiamo poi for-in.
// esso ci permette di passare come argomento del for un array
// senza dover specificare di quanto aumenta la variabile di volta in volta:
// l'interprete capisce che deve aumentare di 1 il contatore a ogni iterazione
// fino a che il valore del contatore non raggiunge la lunghezza dell'array.
// NOTARE: il contatore inizia automaticamente a 0

let giorni = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"];
for (let contatore2 in giorni) {
    console.log(contatore2)
}
console.log()
// da come si nota arriva a 6 perchè l'array "giorni" è composto da 7 elementi.
// partendo da 0 ovviamente contatore2 assume 7 valori diversi

// Infine ci sta il for-of
// che è molto simile al for-in con l'unica e importante eccezione che
// in questo caso il contatore assume il valore corrispondente all'indice
// dell'array invece che assumere l'indice stesso

for (let d of giorni) {
    console.log(d)
}