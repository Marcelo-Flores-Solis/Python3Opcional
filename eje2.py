# Creamos funcion

def calcular_promedio (notas):
    
    #buscamos la peor y mejor nota

    peor_nota = min(notas)
    mejor_nota = max(notas)

    # buscamos el indice de la peor nota

    indice_peor = notas.index(peor_nota)

    # remplazamos la peor nota por la mejor
    notas[indice_peor] = mejor_nota

    # calculamos el nuevo promedio
    promedio = sum(notas) / len(notas)

    return promedio

# Probamos la función con una lista de notas

mis_notas = [12, 15, 17, 14]
print(f"Notas originales: {mis_notas}")

resultado = calcular_promedio(mis_notas)

print ("Notas modificadas: ", mis_notas)
print(f"El promedio modificado es: {resultado}")

#-----------------------------------------------------------

# Probamos la función con otra lista de notas
otras_notas = [10, 20, 15, 18, 14]
print(f"\nNotas originales: {otras_notas}")

resultado2 = calcular_promedio(otras_notas)
print ("Notas modificadas: ", otras_notas)
print(f"El promedio modificado es: {resultado2}")

#-----------------------------------------------------------