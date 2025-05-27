#! /bin/bash

touch pari

# inizio a contare a partire da 1
n=1

# conta nel while fin tanto che n è minore o uguale di 30
while test $n -le 30
do

echo $n

# controlla se il numero è pari o dispari. Fallo con il resto della divisione

if test $[$n % 2] -eq 0

# se il numero contato è pari, inseriscilo nel file pari
then echo $n >> pari
fi

# aggiorna il conto
n=$[$n + 1]

done

echo Conto Finito!
