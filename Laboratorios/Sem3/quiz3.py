vent = 0
nom = input("Nombre: ")
for x in range(0, 3):
	ven = input("Ventas: ")
	vent = int(ven)+vent

com = int(vent)*0.125
print("Vendedor\tVentas\tComision\n--------\t------\t--------\n"+nom+"\t\t"+str(vent)+"\t"+str(com))