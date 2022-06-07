import sys
#Validar si hay dos notas o no...

if len(sys.argv) == 3:
	nota1 = int(sys.argv[1])
	nota2 = int(sys.argv[2])

	if nota1 < 10 or nota2 < 10 or nota1 > 0 or nota2 > 0:
		if (nota1 + nota2) / 2 > 4:
			print("aprobaste zafando")
		else:
			print("no aprobaste")
	else:
		print("notas fuera de rango")

else:

	print("Paremtros incorrectos")