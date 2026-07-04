from pdf_utils import leer_pdf, dividir_texto
from embeddings import generar_vectores
from controlador import crear_coleccion, guardar_vectores

ruta_pdf = "metamorfosis.pdf"  #Direccion de l PDF


print("Leyendo PDF...")
texto = leer_pdf(ruta_pdf)


print("Dividiendo texto...")
chunks = dividir_texto(texto)


print("Generando vectores...")
vectores = generar_vectores(chunks)


print("reando colección...")
crear_coleccion("metamorfosis")


print("Guardando en Qdrant...")
guardar_vectores("metamorfosis", chunks, vectores)


print("🚀 PROCESO COMPLETADO")
