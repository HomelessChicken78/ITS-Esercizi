#! /bin/bash

mkdir planets


# a ogni iterazione p assume come valore in sequenza ciascuno dei valori indicati (in questo caso i pianeti del sistema solare
for p in mercurio venere terra marte giove saturo urano nettuno
do
	# crea un file dentro la cartella "planets" chiamata come il valore che assume in quel momento la variabile p
	touch planets/$p
done
