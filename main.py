from tkinter.filedialog import askdirectory


from metadatos.crear_metadatos import Archivo_Pdf


def ejecutar(ruta):
    pdf = Archivo_Pdf(ruta)
    pdf.crear_metadatos()

ejecutar(askdirectory())
