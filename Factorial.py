# Import math Library
import math

#Creem la variable Factorial on obtindrem el resultat de l'operació
Factorial =1

#Demanem el número del qui volem calcular el seu factorial
print('Indica el número per calcular el seu factorial')
num=int(input())
  
# num!=num*(num-1)*(num-2)*.....*1  
for i in range(num):
    Factorial=Factorial+Factorial*i
    
#Mostra el resultat    
print(Factorial)

#Fem servir la biblioteca math per calcular el factorial
print('\n','EL factorial de',num,'és')

#Mostra el resultat
print(math.factorial(num))
