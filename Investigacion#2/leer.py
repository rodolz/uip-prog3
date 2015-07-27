import shutil
import sys
with open("asd.txt", "r") as f:  #Abrimos el archivo de texto asd.txt para imprimi
	shutil.copyfileobj(f, sys.stdout)
