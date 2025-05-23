// Un array è una collezione di valori.

// Per definirlo è possibile fare:
let a1 = [
    "lunedi",
    "martedi",
    "mercoledi",
    "giovedi",
    "venedi",
    "sabato",
    "domenica"
]

let index = 4
console.log(a1)
console.log(a1[index])  // accesso a un singolo elemento dell'array con un indice

a1.push("javascriptledi")  // aggiunge un nuovo elemento alla fine dell'array
console.log(a1)

let n = 1
a1.splice(0, n) // Rimuove n elementi dall'array a partire dall'indice 0
console.log(a1)