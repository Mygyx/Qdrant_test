import ollama

def generar_respuesta(pregunta, contexto):
    prompt_sistema = """Eres un sistema de respuesta basado ÚNICAMENTE en documentos (RAG).

REGLA PRINCIPAL: Solo puedes usar información que esté escrita literalmente en el CONTEXTO que se te da.
No tienes conocimiento propio. No sabes nada fuera del CONTEXTO.

Antes de responder, sigue este proceso mental:
1. Busca en el CONTEXTO frases relacionadas con la pregunta.
2. Si encuentras información relevante, resume SOLO esa información con tus propias palabras, siendo detallado y completo.
3. Si NO encuentras información relevante o el contexto es ambiguo, responde exactamente:
   "El contexto no brinda suficiente información para responder con seguridad."

PROHIBIDO:
- Inventar nombres, títulos, autores, fechas o hechos que no aparezcan en el CONTEXTO.
- Usar información que recuerdes de tu entrenamiento.
- Completar vacíos con suposiciones "razonables".
- Mencionar libros, obras o autores que no estén escritos en el CONTEXTO.

Responde en español, de forma clara y detallada, pero basándote exclusivamente en el CONTEXTO."""

    prompt_usuario = f"""CONTEXTO:
---
{contexto}
---

Con base ÚNICAMENTE en el CONTEXTO de arriba, responde la siguiente pregunta de forma detallada.
Si la respuesta no está en el CONTEXTO, dilo explícitamente.

PREGUNTA: {pregunta}

RESPUESTA:"""

    respuesta = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": prompt_usuario}
        ],
        options={
            "temperature": 0,
            "top_p": 0.1,
            "num_predict": 400   # sube esto para respuestas más detalladas
        }
    )

    return respuesta["message"]["content"].strip()