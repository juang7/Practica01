# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import time # libreria necesaria para pausar

i=99
s="'99 Bottles of Beer'\n" # guardamos la cadena en una variable

print  s.center(62) #centramos la cadena guardada en la variable s

while i>0:
    print "\n",i,"bottles of beer on the wall,", i,"""bottles of beer.
Take one down, pass it around,""",i-1,"bottles of beer on the wall."
    i=i-1 
    time.sleep(3) #Utilizamos para que nos de tiempo cantar antes de la aparicion del proximo verso

# <codecell>


