preg=input("Ejecutar el programa? (S/N)\n")
cifrada = []
cifrada2 = []
cifrada3 = []
descifrada = []
cont=0
while preg=="s" or preg=="S":
	cond=input("Elija: 1. Introducir 2. Cifrar  3. Descifrar 4. LIMPIAR LISTAS  5. Imprimir 6. Salir\n")
	if cond == "1":
		palabra=input("Introduzca el texto: \n") # Se introduce la palabra, ya sea sin cifrar o cifrada
	elif cond == "2": 
		for x in palabra:
			cif=ord(x)+1 		# Se cifra la palabra introducida en el cond==1
			cifrada.append(cif)
		for x in cifrada:
			des=chr(x)
			cifrada2.append(des)
	elif cond == "3":
		for x in cifrada2:
			cif=ord(x)-1  		# Se descifra la palabra introducida en el cond==1
			cifrada3.append(cif)
		for x in cifrada3:
			des=chr(x)			# Se convierte en texto la palabra descrifrada
			descifrada.append(des)
	elif cond == "4":         # En este paso se limpian las listas, necesario para descifrar varias palabras
		cifrada = []
		cifrada2 = []
		cifrada3 = []
		descifrada = []
	elif cond == "5":
		preg2=0
		while preg2<3:
			preg2=int(input("Opciones: 1. Texto cifrado 2. Texto descrifrado 3. Salir\n"))
			if preg2 == 1:
				res = ''.join(cifrada2) # Se imprime la lista cifrada
				print(res)
				print("\nAcuerdese de limpiar las listas si va a cifrar o descifrar varias palabras")
			elif preg2 == 2:
				res = ''.join(descifrada) # Se imprime la lista descifrada
				print(res)
				print("\nAcuerdese de limpiar las listas si va a cifrar o descifrar varias palabras")
	else:
		break