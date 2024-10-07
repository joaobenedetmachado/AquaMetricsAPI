from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

minhaSenha = '123'
client = MongoClient(f"mongodb+srv://joaoteste:{minhaSenha}@iotcluster.a70ey.mongodb.net/?retryWrites=true&w=majority&appName=IotCluster")
db = client["aqua"]
collection = db["aquacollections"]

app = FastAPI()

class Documento(BaseModel):
    data: str
    ph: str  # string
    tds: str  # string
    temp: str  # string

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
    novo_documento = documento.dict()  # Converte o modelo para dicionário
    resultado = collection.insert_one(novo_documento)
    return {"message": "Documento inserido", "id": str(resultado.inserted_id)}