/*Esercizio 4.2
Scrivere un programma che stampa i
numeri da 0 a 10 sia con il ciclo for che
con il ciclo while;*/

let counter = 0
console.log("Con il while:")
while (counter <= 10) {
    console.log(counter)
    counter++
}

console.log("\nCon il for:")
for (let i = 0; i <= 10; i++) {
    console.log(i)
}