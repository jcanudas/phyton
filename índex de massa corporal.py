#Programa Índex de massa corporal
#Demanem les dades de pes i altura per poder calcula l'imc

pes= float(input('Indica el teu pes en kg: '))
altura= float(input('Indica la teva alçada en m: '))

#Calculem l'imc i l'arrodonim a una xifra decimals

imc= round((pes/(altura)**2),1)

# Presentem el resultat
# Hem canviat la ' per la " per poder posar l'apòstrof

print ("L'índex de massa corporal (imc) és",imc)

#Analitzem el resultat per determinar si hi ha pes baix, normal o sobrepès

if (imc>=25):
    print('Aquest valor indica sobrepès')
elif (imc<18.5):
    print('Aquest valor indica un pes baix')
else:
    print('Aquest valor indica un pes normal')

          