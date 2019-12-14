import os.path as path 





def crear_archivo_txt(datos_pdf, ruta_archivo = "metadatos.txt"):
	
	datos = datos_pdf
	
	if path.exists(ruta_archivo):
		leer_archivo_txt()
	else:
		escribir_archivo_txt(datos, ruta_archivo)
		

def leer_archivo_txt():
	print("leyendo")

def escribir_archivo_txt(datos, nombre):

	archivo_r = open(nombre, "w")
	archivo_r.write(datos)
	archivo_r.close() 
	print("archivo creado")