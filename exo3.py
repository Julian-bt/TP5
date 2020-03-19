#affichage des éléments d'une liste

i=0
listSeance=[29, 'a', 22, 3.14, 35, 'b', "ISEN Bretagne", 56, 44]
print(len(listSeance))#affiche le nombre de groupe dans la chaine

while i<9:
    x=listSeance[i:i+1]
    print(x)
    i=i+1
