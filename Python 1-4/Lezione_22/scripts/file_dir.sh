#! /bin/bash

if test -f $1
then echo "$1 esiste ed è un file"
else echo "$1 non esiste oppure non è un file"
fi

if test -d $2
then echo "$2 esiste ed è una directory"
else echo "$2 non esiste oppure non è una directory"
fi
