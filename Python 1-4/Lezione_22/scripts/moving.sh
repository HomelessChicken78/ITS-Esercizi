#! /bin/bash

if test -f $1 -a -d $2
then mv $1 $2 && echo "$1 è stato spostato nella directory $2"
else echo "Non posso spostare $1 dentro $2"
fi
