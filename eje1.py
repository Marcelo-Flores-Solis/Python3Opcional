#Pedimos información al usuaio
usuario = input("Ingrese el nombre de usuario: ")
dominio = input("Ingrese el dominio: ")

#Imprimimos el mensaje tomando en cuenta las restricciones
#Primera forma encontrada print(f"{usuario}@{dominio}")
#-----------------------------------------------------------

#Segunda forma encontrada usando tuplas 

partes = (usuario, "@", dominio)
# Unimos la tupla usando una cadena vacía como pegamento
print("".join(partes))

#-----------------------------------------------------------


