from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient

minhaSenha = '123'
client = MongoClient(f"mongodb+srv://joaoteste:{minhaSenha}@iotcluster.a70ey.mongodb.net/?retryWrites=true&w=majority&appName=IotCluster")
db = client["aqua"]
collection = db["aquacollections"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # Adiciona a origem local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Documento(BaseModel):
    data: str
    ph: str  # string
    tds: str  # string
    temp: str  # string

@app.get("/documentos") # quando a rota for um get, ele faz isso:
async def lerDocumentos():
    documentos = []
    cursor = collection.find({}) # le com o .find do collection
    for documento in cursor:
        documento['_id'] = str(documento['_id'])  
        documentos.append(documento)
    return {"documentos": documentos}

@app.post("/documentos") # quando a rota for um post, faz isso:
async def inserirDocumentos(documento: Documento):
    novo_documento = documento.dict()  # converte o modelo para dicionário
    resultado = collection.insert_one(novo_documento) # e aqui ele pega o documento e manda pro DB com o insert_one
    return {"message": "Documento inserido", "id": str(resultado.inserted_id)}
