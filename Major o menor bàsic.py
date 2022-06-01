# Demanem a l'usuari el valor que volem analitzar
# Desem el valor a la variable num

num= float(input('Número: '))

#Comparem el valor desat a num amb 0 per saber si és positiu o negatiu

if num > 0:
    print(("El número:",num, "és",'positiu'))
elif num < 0:
    print(("El número:",num, "és",'negatiu'))
else:
    print("El número:",num, "és",'0')
    
