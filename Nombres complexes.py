# Import cmath Library (llibreria per treballar nombres complexos 
import cmath


# Escollim l'opció que volem
print('Escull quina operació vols realitzar','\n','1.- Passar de binòmica a polar','\n','2.- Passar de polar a binòmica')
while True:
    opcio=int(input())
    if opcio == 1 or opcio == 2:
        break
    
# Passar de binòmica a polar    
if opcio== 1:
    print('a + bj')
    a= float(input('a '))
    b=float(input('b '))
    binomica=complex(a,b)
    polar=cmath.polar(binomica)
    print(polar)

# Passar de polar a binòmica
if opcio== 2:
    print('modul i fase(radians)')
    modul= float(input('a '))
    fase=float(input('b '))
    binomica = cmath.rect(modul, fase)
    print(binomica)
    




