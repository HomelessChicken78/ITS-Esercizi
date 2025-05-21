#! /bin/bash

echo "Scrivi il primo numero"
echo "->"
read n1

echo "Scrivi il secondo numero"
echo "->"
read n2

echo $(($n1*$n2))
