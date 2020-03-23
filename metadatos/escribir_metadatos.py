from ayuda.pdf import ArchivoPdfLectura
from ayuda.lectura_metadatos import ArchivoMetadatos

class Comparador:

    def __init__(self, directorio_de_recibos):

        
        pdf = ArchivoPdfLectura(directorio_de_recibos)
        self.datos_recibos = pdf.leer_pdf()

        txt = ArchivoMetadatos('C:\\RECIBOS_METADATOS\\metadatos.txt')
        self.datos_txt = txt.leer()

    def comparacion(self):

    
    def escribir_metadatos(self.)