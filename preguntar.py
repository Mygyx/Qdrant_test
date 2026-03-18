from controlador import buscar_en_pdf

pregunta = input("Haz una pregunta: ")

resultados = buscar_en_pdf(pregunta)

# 🔥 unir contexto
contexto = " ".join(resultados)

print("\n🤖 Respuesta:\n")

# respuesta simple (sin IA todavía)
print(f"Basado en el texto:\n{contexto[:500]}...")
