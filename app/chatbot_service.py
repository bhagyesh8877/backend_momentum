from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid

router = APIRouter()

class ChatStartInput(BaseModel):
    asset_id: str

class ChatMessageInput(BaseModel):
    chat_thread_id: str
    message: str


chat_history = {}

@router.post("/start")
async def start_chat(chat_start: ChatStartInput):
    chat_thread_id = str(uuid.uuid4())
    chat_history[chat_thread_id] = []
    return {"chat_thread_id": chat_thread_id}

@router.post("/message")
async def chat_message(chat_message: ChatMessageInput):
    chat_thread_id = chat_message.chat_thread_id
    user_message = chat_message.message

    if chat_thread_id not in chat_history:
        raise HTTPException(status_code=404, detail="Chat thread not found")

    
    response = f"Response for '{user_message}' with asset ID: {chat_thread_id}" 
    chat_history[chat_thread_id].append({"user": user_message, "agent": response})
    return {"response": response}

@router.get("/history")
async def get_chat_history(chat_thread_id: str):
    if chat_thread_id not in chat_history:
        raise HTTPException(status_code=404, detail="Chat thread not found")

    return {"chat_history": chat_history[chat_thread_id]}
