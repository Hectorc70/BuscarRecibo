from tkinter.filedialog import askdirectory


from metadatos.crear_metadatos import Archivo_Pdf
from extractor.buscador_recibo import Recibo


def ejecutar(ruta):
    pdf = Archivo_Pdf(ruta)
    pdf.extraer_no_control()

def extraer_recibo():
    reci = Recibo("300596", "01", "2")
    reci.leer_archivo()
extraer_recibo()
#ejecutar(askdirectory())
