// "if" permette di valutare condizioni ed eseguire il codice se l'istruzione è vera. 
// Le condizioni vengono verificate con un booleneano:
// se è true ciò che è nell'if viene eseguito.

let money = 50
if (money > 40){
    console.log(`Puoi acquistare questo prodotto del costo di 40€. Hai infatti ${money}€ al momento.`)
}

// Le if possono essere seguite da un "else".
// In questo caso se la condizione risulta esser falsa, verrà eseguito quello che si trova nell'else invece che non fare nulla

if (money > 70){
    console.log(`Puoi acquistare questo prodotto del costo di 70€. Hai infatti ${money}€ al momento.`)
} else {
    console.log(`Non puoi acquistare un prodotto che costa 70€, hai solo ${money}€`)
}

// infine l'else if è una condizione di mezzo. L'interprete valuta prima l'if.
// Se è falso valuta il prossimo else if.
// Se falso anche questo valuta il prossimo else if e cosi via finchè tutti
// gli else if finiscono e a quel punto l'interprete esegue l'else (se esiste)

let age = 21
if (age < 18) {
    console.log("Sei un ragazzo/bambino.")
} else if (age >= 18 && age < 70){
    console.log("Sei un adulto.")
} else {
    console.log("Sei un anziano.")
}