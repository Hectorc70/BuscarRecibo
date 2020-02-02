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
		
		archivo_r = open(nombre, "r")
		datos_txt = archivo_r.readlines()
		
		for dato in datos_txt:			
			if dato.split('|')[0] == datos.split('|')[0]:
				print("los datos ya existen")
			
			else:
				archivo_r = open(nombre, "w")
				archivo_r.write(datos)
				print("leido y escrita la INFO")

		archivo_r.close() 
		

	def escribir_archivo_txt(self, datos, nombre):

		archivo_r = open(nombre, "w")
		archivo_r.write(datos)
		archivo_r.close() 
		print("archivo creado")