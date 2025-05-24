/*Esercizio 4.3
Modificare l'esercizio 2 in modo che
stampa i numeri da 5 a 15 sia con il
ciclo for che con il ciclo while;*/

let counter = 5
console.log("Con il while:")
while (counter <= 15) {
    console.log(counter)
    counter++
}

console.log("\nCon il for:")
for (let i = 5; i <= 15; i++) {
    console.log(i)
}