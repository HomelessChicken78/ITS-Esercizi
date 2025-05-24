// while e while do sono due tipologie di iterazione.
// Un'iterazione ripete una sequenza di step finche' una condizione è soddisfatta (o insoddisfata).
// Quindi un'iterazione permette con poche righe di codice di ripetere
// 10, 30 o un numero indefinito di volte una sequenza finita di istruzioni

// il while ripete le istruzioni al suo interno
// fin tanto che la condizione definita all'inizio è vera (quindi con valore "true").
// Dal momento che diviene "false"
// (per via di un cambiamento dello stato delle variabili nel while all'interno del ciclo stesso)
// il ciclo finisce e l'interprete prosegue con le istruzioni fuori dal while


let contatore = 0 
while (contatore <= 3){
    console.log(contatore)
    contatore++  // Incrementa il contatore, così eventualmente la condizione "contatore <= 3" diventa false e il ciclo finisce (altrimenti il ciclo sarebbe infinito)
}
console.log("Finito!")

// do while è molto simile al while con una sola eccezione:
// esegue le istruzioni al suo interno almeno una volta.
// infatti un while può anche non fare nemmeno una volta le istruzioni se la condizione è subito false


let contatore2 = 1
// Non verrà mai eseguito
while (false) {
    console.log(`Ho eseguito ${contatore2} volte l'iterazione`)
    contatore2++
}

// anche se la condizione è false, l'iterazione viene eseguita almeno una volta a prescindere
do {
    console.log(`Ho eseguito ${contatore2} volte l'iterazione`)
    contatore2++
}
while (false)

// questo perchè nel do-while la condizione viene verificata DOPO l'esecuzione delle istruzioni, non prima