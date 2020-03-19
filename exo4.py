#Ajout/modification/supression d'éléments d'une liste

listMonths=['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'semptembre', 'octobre', 'novembre', 'decembre']
listDaysPerMonths=[31, 28, 31, 30, 31, 30,31, 30, 31, 30, 31]
liste=[] #liste vide

taille=len(listDaysPerMonths)#affiche le nombre de groupe dans la chaine

for i in range(0,taille):
    liste.append(listMonths[i])
    liste.append(listDaysPerMonths[i])
print(liste)
