tele =  {}
preg=input("Ejecutar el programa? (S/N)\n")
while preg=="s" or preg=="S":
	cond=input("Elija: 1. Imprimir 2. Agregar  3. Quitar 4. Buscar  5. Salir\n")
	if cond == "1":
		print("Numeros telefonicos: \n")
		for nom in tele.keys():
   			print(nom+":"+str(tele[nom])+"\n")
	elif cond == "2":
		nom=input("Nombre:\n")
		num=input("Numero:\n")
		tele[nom] = int(num)
	elif cond == "3":
		print("Quitar Nombre y Numeros\n")
		nom=input("Diga el Nombre a eliminar\n")
		del tele[nom]
	elif cond == "4":
		print("Buscar numeros\n")
		nom=input("Diga el Nombre a buscar\n")
		print("Su numero es: "+str(tele[nom])+"\n")
	else:
		print("Gracias por usar el programa\n")
		break
