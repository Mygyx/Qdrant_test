from pypdf import PdfReader

def leer_pdf(ruta):
    reader = PdfReader(ruta)
    texto = ""

    for page in reader.pages:
        contenido = page.extract_text()
        if contenido:
            texto += contenido

    return texto


def dividir_texto(texto, tamaño=500):
    chunks = []

    for i in range(0, len(texto), tamaño):
        chunks.append(texto[i:i+tamaño])

    return chunks