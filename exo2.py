#boucle et concaténation

a=int(input("nombre de ligne: "))
i=0
etoile="******************************************************************************************" #je vais pas pouvoir afficher plus d'étoile que je viens de mettre

while i<=a:
        Resultat=etoile[0: i+1]
        print(Resultat)
        i=i+1

#ou autre méthode
nbligne=int(input("nombre de ligne: "))
for i in range(1, nbligne+1):
    print(i* "*" )


#ou
etoile='*'
i=1

while i<11:
    print(i*etoile)
    i=i+1
while i!=0:
    print(i*etoile)
    i=i-1
