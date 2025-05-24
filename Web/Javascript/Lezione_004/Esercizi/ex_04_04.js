/*Esercizio 4.4
Scrivere un programma che conta da 0
a 20 con passo 2 e stampa i numeri
ottenuti (0,2,...,20) sia con il ciclo for
che con il ciclo while ;*/

let counter = 0
console.log("Con il while:")
while (counter <= 20) {
    console.log(counter)
    counter += 2
}

console.log("\nCon il for:")
for (let i = 0; i <= 20; i+=2) {
    console.log(i)
}
