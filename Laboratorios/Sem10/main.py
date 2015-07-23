from Autor import Autor
from Libro import Libro
from Copia import Copia
from Lector import Lector

copiaXlibros = 10
lec,cop,lib,aut,registro = {},{},[],{},{}
opciones = ("1. Ingresar un lector.","2. Ingresar un autor.","3. Ingresar un libro.", "4. Hacer peticion.", "5. Hacer devolucion. 6. Salir")

print("\n\n\tBienvenido")
for indice in opciones:
	print(indice)
while True:
	opcion = int(input("Ingrese una opcion."))
	if opcion == 1:
		nombrE = input("Ingrese el nombre: ")
		iD = input("Ingrese el id: ")
		L = Lector(iD,nombrE)
		lec[L.nombre]= L.id
		continue

	elif opcion == 2:
		nombrE = input("Ingrese el nombre: ")
		nacionalidaD = input("Ingrese la nacionalidad: ")
		A = Autor(nombrE,nacionalidaD)
		aut[A.nombre]= A.nacionalidad
		continue

	elif opcion == 3:
		titulO = input("Ingrese el titulo: ")
		tipO = input("Ingrese el tipo: ")
		editoriaL = input("Ingrese la editorial: ")
		Lb = Libro(titulO, tipO, editoriaL)
		lib.append(Lb.titulo)
		continue

	elif opcion == 4:
		nombres = lec.keys()
		i = input("Diga su Nombre:")
		for keys in lec:
			if keys==i:
				print("Bienvenido "+i)
		l = input("Que libro desea? (Titulo) ")
		for indice in lib:
			if indice==l:
				print(i+" solicitastes el libro "+l)
		registro[i]=l
		continue

	elif opcion == 5:
		print("Devolucion de libros")
		i = input("Diga su nombre:")
		for keys in registro:
			if keys==i :
				print("Gracias por su devolucion")
				del registro[i]
		print(registro)
		continue
	else:
		print("Saliendo del programa")
		input()
		break