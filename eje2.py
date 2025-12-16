# Creamos funcion

def calcular_promedio (notas):
    
    #sumamos las notas 
    suma = sum(notas)

    #buscamos la peor y mejor nota

    peor_nota = min(notas)
    mejor_nota = max(notas)

    # calculamos una nueva suma

    nueva_suma = suma - peor_nota + mejor_nota

    # Promedio
    promedio = nueva_suma / len(notas) 

    return promedio

# Probamos la función con una lista de notas
mis_notas = [12, 15, 17, 14]
resultado = calcular_promedio(mis_notas)

print(f"El promedio modificado es: {resultado}")

#-----------------------------------------------------------

# Probamos la función con otra lista de notas
otras_notas = [10, 20, 15, 18, 14]
resultado2 = calcular_promedio(otras_notas)
print(f"El promedio modificado es: {resultado2}")