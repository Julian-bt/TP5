#lapinty


U0=0
U1=1
i=1

while i<25:
    U2=U1+U0
    U0=U1
    U1=U2

    print("nombre de lapin au mois", i, "est ", U2)
    i=i+1

