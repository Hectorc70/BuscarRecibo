from tkinter.filedialog import askdirectory

from ayuda.pdf import ArchivoPdfLectura
from ayuda.lectura_metadatos import ArchivoMetadatos
from ayuda.txt import ArchivoTxt

class Comparador:

    def __init__(self, directorio_de_recibos):

        
        pdf = ArchivoPdfLectura(directorio_de_recibos)
        self.datos_recibos = pdf.leer_pdf()

        txt = ArchivoMetadatos('C:\\RECIBOS_METADATOS\\metadatos.txt')
        self.datos_txt = txt.leer()

    def comparacion(self):

        control_recibos = self.convertir_a_lista(self.datos_recibos.keys())
        control_metadatos = self.convertir_a_lista(self.datos_txt.keys())
        
        for control in control_recibos:
            if not control in control_metadatos:
                self.escribir_metadatos(self.datos_recibos)

            

    def convertir_a_lista(self, diccionario):

        lista_convertida = list()

        for item in diccionario:
            
            lista_convertida.append(item)
        return lista_convertida

    def escribir_metadatos(self, datos):

        for control, datos in datos.items():
            pagina = datos[0]
            periodo = datos[1]
            ruta = datos[2]



            archivo_metadatos = ArchivoTxt('C:\\RECIBOS_METADATOS\\metadatos.txt')

        archivo_metadatos.escribir(datos)

escribir = Comparador(askdirectory())
escribir.comparacion()