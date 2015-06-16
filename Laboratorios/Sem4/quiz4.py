lista =  []
cont=1
preg=input("Desea crear la lista? (s/n)\n")
while preg=="s" or preg=="S":

	lista.append(input("Item #"+str(cont)+"\n"))
	cont=cont+1
	preg=input("Agregar otro item? (S/N)\n")

preg=input("Elija: 1.Agregar 2.Eliminar 3.Ver\n")
if preg == "1":
	lista.append(input("Item adicional\n"))
elif preg == "2":
	num=input("Selecciona el # del item a eliminar\n")

	del lista[int(num)-1]

print("Esta es su Lista\n")
print(lista)