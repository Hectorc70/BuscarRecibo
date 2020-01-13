from tkinter.filedialog import askdirectory


from metadatos.crear_metadatos import Archivo_Pdf


def ejecutar(ruta):
    pdf = Archivo_Pdf(ruta)
    pdf.extraer_no_control()

ejecutar(askdirectory())
