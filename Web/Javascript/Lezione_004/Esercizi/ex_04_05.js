/*Esercizio 4.5
Modificare l'esercizio 4 in modo che
stampi il doppio dei numeri ottenuti
(0,4,...,40) sia con il ciclo for che con il
ciclo while;*/

let counter = 0
console.log("Con il while:")
while (counter <= 20) {
    console.log(counter*2)
    counter += 2
}

console.log("\nCon il for:")
for (let i = 0; i <= 20; i+=2) {
    console.log(i*2)
}