# Programa countdown
# Un programa modificat a partir del programa countdown_bàsic.py
# El programa farà un compte enrera des del valor donat fins a zero

# Hem definit la funció countdown

def countdown(i):
    while i > 0:
        print(str(i))
        i -= 1
# Demanem el valor a partir del qual fa el compte enrere
# El nombre introduït ha de ser un nombre sencer (int)

N= int(input('Número: '))

#Cridem la funció countdown

countdown(N)