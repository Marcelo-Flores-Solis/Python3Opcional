# Creamos funcion

def calcular_promedio (notas):
    
    #sumamos las notas 
    suma = sum(notas)

    #buscamos la peor y mejor nota

    peor_nota = min(notas)
    mejor_nota = max(notas)

    # calculamos una nueva suma

    nueva_suma = suma - peor_nota - mejor_nota

    # Promedio
    promedio = nueva_suma / len(notas) 

    return promedio