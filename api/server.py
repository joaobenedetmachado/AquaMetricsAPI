from fastapi import FastAPI
from pymongo import MongoClient

# Conexão com MongoDB
minhaSenha = '123'
client = MongoClient(f"mongodb+srv://joaoteste:{minhaSenha}@iotcluster.a70ey.mongodb.net/?retryWrites=true&w=majority&appName=IotCluster")
db = client["aqua"]
collection = db["aquacollections"]

# Criação da instância FastAPI
app = FastAPI()

# Rota para ler documentos do MongoDB
@app.get("/documentos")
async def ler_documentos():
    documentos = []
    cursor = collection.find({})
    for documento in cursor:
        documento['_id'] = str(documento['_id'])  # Convertendo ObjectId para string
        documentos.append(documento)
    return {"documentos": documentos}

# Rota para inserir um novo documento no MongoDB
@app.post("/documentos")
async def inserir_documento(data: str, ph: str, tds: str, temp: str):
    novo_documento = {
        "data": data,
        "ph": ph,
        "tds": tds,
        "temp": temp
    }
    resultado = collection.insert_one(novo_documento)
    return {"message": "Documento inserido", "id": str(resultado.inserted_id)}
