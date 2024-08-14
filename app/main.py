from fastapi import FastAPI
from app.document_processing import router as document_processing_router
from app.chatbot_service import router as chatbot_service_router

app = FastAPI()

app.include_router(document_processing_router, prefix="/api/documents")
app.include_router(chatbot_service_router, prefix="/api/chat")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
