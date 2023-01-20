# Demanem a l'usuari el valor del costat d'un triangle
# Dibuixem el triangle amb *

num= int(input('Número: '))

#EL nombre de files = número introduït
for i in range(num):
#Per ca línia
    for x in range(i+1):
        print('*', end=(' '))
#Salt de línia       
    print('')