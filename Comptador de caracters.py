# Programa Comptador de caràcters
# Aquest programa compte el nombre de vocals, espais en blanc i consonants

# Definim la frase a analitzar
frase = 'La frase del dia'

# Declarem les variables
vocals= 'aeiouAEIOU'

# Obtenim la longitud de la cadena
longitud= len(frase)

nombre_vocals=0
nombre_espais=0

# Comparem cada caràcter de la frase amb les vocals i amb un espai en blanc
# Si no és cap vocal, ni espai en blanc llavors considerem que és una consonant
# Aquest programa no consideraria les vocals accentuades com a vocals


for i in range(0,longitud):
    if frase[i] in vocals:
        nombre_vocals +=1
    elif frase[i] in ' ':
        nombre_espais +=1
        
#Calculem el nombre de consonants        
nombre_consonants= longitud - nombre_vocals - nombre_espais

#Presentem els resultats
print('Aquesta frase té',nombre_vocals, 'vocals'',',nombre_consonants,'consonants i',nombre_espais,'espais en blanc')

