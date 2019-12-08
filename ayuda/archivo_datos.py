import os.path as path 




def crear_archivo_txt():


	if path.exists(ruta_destino):
		leer_archivo_txt()
	else:
		archivo_r = open("metadatos.txt" "r") 

def leer_archivo_txt():
	print("leyendo")