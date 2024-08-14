from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import chromadb
from langchain.embeddings import OpenAIEmbeddings

router = APIRouter()

class DocumentInput(BaseModel):
    file_path: str


vector_db = chromadb.Client()
collection = vector_db.create_collection("documents")

@router.post("/process")
async def process_document(document: DocumentInput):
    if not os.path.exists(document.file_path):
        raise HTTPException(status_code=400, detail="File not found")

    
    with open(document.file_path, "r", encoding="utf-8") as file:
        content = file.read()

   
    embeddings = OpenAIEmbeddings().embed_text(content)

  
    asset_id = f"asset_{os.path.basename(document.file_path)}"
    collection.add(asset_id, embeddings)

    return {"asset_id": asset_id}
