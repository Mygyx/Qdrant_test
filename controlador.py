from embeddings import modelo
from conexion_qdrant import obtener_cliente

def verificar_conexion():
    try:
        client = obtener_cliente()
        colecciones = client.get_collections()
        
        return {
            "estado": "ok",
            "colecciones": colecciones.collections
        }
    except Exception as e:
        return {
            "estado": "error",
            "mensaje": str(e)
        }
    

def crear_coleccion(nombre):
    client = obtener_cliente()

    client.recreate_collection(
        collection_name=nombre,
        vectors_config={
            "size": 384,
            "distance": "Cosine"
        }
    )

    print("✅ Colección creada")


def guardar_vectores(nombre_coleccion, chunks, vectores):
    client = obtener_cliente()

    puntos = []

    for i, vector in enumerate(vectores):
        puntos.append({
            "id": i,
            "vector": vector.tolist(),
            "payload": {
                "texto": chunks[i]
            }
        })

    client.upsert(
        collection_name=nombre_coleccion,
        points=puntos
    )

    print("✅ Datos guardados en Qdrant")    

def buscar_en_pdf(pregunta, coleccion="metamorfosis"):
    client = obtener_cliente()

    vector = modelo.encode(pregunta)

    resultados = client.query_points(
        collection_name=coleccion,
        query=vector,
        limit=3
    )

    textos = []

    # 👇 ESTA ES LA FORMA CORRECTA
    for punto in resultados.points:
        textos.append(punto.payload["texto"])

    return textos