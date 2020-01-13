import os.path as path 



class ArchivoTxt:

	def __init__(self, texto, archivo = "metadatos.txt"):
		self.texto 		  = texto
		self.ruta_archivo = archivo
		self.crear_archivo_txt()	

	def crear_archivo_txt(self):
				
		
		if path.exists(self.ruta_archivo):
			self.leer_archivo_txt(self.texto, self.ruta_archivo)
		else:
			self.escribir_archivo_txt(self.texto, self.ruta_archivo)
		

	def leer_archivo_txt(self, datos, nombre ):
		
		archivo_r = open(nombre, "a")
		archivo_r.write('\n' + datos)
		
		archivo_r.close() 
		print("leido y escrita la INFO")

	def escribir_archivo_txt(self, datos, nombre):

		archivo_r = open(nombre, "w")
		archivo_r.write(datos)
		archivo_r.close() 
		print("archivo creado")