from qdrant_client import QdrantClient

def obtener_cliente():
    return QdrantClient(host="localhost", port=6333)