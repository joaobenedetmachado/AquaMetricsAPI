from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

minhaSenha = '123'
client = MongoClient(f"mongodb+srv://joaoteste:{minhaSenha}@iotcluster.a70ey.mongodb.net/?retryWrites=true&w=majority&appName=IotCluster")
db = client["aqua"]
collection = db["aquacollections"]

app = FastAPI()

class Documento(BaseModel):
    data: str
    ph: str
    tds: str
    temp: str

@app.get("/documentos")
async def ler_documentos():
    documentos = []
    cursor = collection.find({})
    for documento in cursor:
        documento['_id'] = str(documento['_id'])  
        documentos.append(documento)
    return {"documentos": documentos}

@app.post("/documentos")
async def inserir_documento(documento: Documento):
    novo_documento = {
        "data": documento.data,
        "ph": documento.ph,
        "tds": documento.tds,
        "temp": documento.temp
    }
    resultado = collection.insert_one(novo_documento)
    return {"message": "Documento inserido", "id": str(resultado.inserted_id)}
