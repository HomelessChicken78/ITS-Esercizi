#! /bin/bash

echo "Premi un tasto e poi premi invio: "

read test

case $tasto in
[a-z] ) echo "lettera"
[0-9] ) echo "numero"
* ) echo "Punteggiatura, spaziatura o altro"
esac
