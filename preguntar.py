from controlador import buscar_en_pdf
from modelo_Ollama import generar_respuesta 


while True:
    mensaje = input("Escribe 'salir' para terminar o presiona Enter para continuar: ")
    if mensaje.lower() == "salir":
        break
    pregunta = input("Haz una pregunta: ")

    resultados = buscar_en_pdf(pregunta)

    contexto = " ".join(resultados)

    print("\nRespuesta:\n")

    respuesta = generar_respuesta(pregunta, contexto)

    print(f"Pregunta: {pregunta}\n")
    print(f"Respuesta: {respuesta}\n")
