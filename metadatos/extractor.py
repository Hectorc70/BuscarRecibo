from tkinter.filedialog import askdirectory, asksaveasfilename

from PyPDF2 import PdfFileReader, PdfFileWriter

from buscador_recibo import ArchivoMDatos



class ReciboPDF:

    def __init__(self, control, ruta, ruta_destino):
        
        self.ruta_destino = ruta_destino
        archivo     = ArchivoMDatos(control, ruta)
        self.datos_pdf   = archivo.leer_archivo()   

    def extraer_hoja(self):

        ruta_pdf = self.datos_pdf[0]
        pagina   = self.datos_pdf[1]

        pdf_original =PdfFileReader(ruta_pdf,'rb')
        pdf_nuevo = PdfFileWriter()
        pdf_nuevo.addPage(pdf_original.getPage(pagina))
        
        self.guardar_archivo(self.ruta_destino, pdf_nuevo)



    def guardar_archivo(self, ruta, pdf):
        #ruta_pdf_nuevo = ruta + 'new'

        pdf.write(ruta)


recibo = ReciboPDF('00310314', askdirectory(), asksaveasfilename())
recibo.extraer_hoja()