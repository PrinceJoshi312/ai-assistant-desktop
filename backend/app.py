from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas import ChatRequest, ChatResponse
from backend.chatbot_engine import predict_intent, get_static_response, gemini_reply
from backend.tasks_api import map_task

# ✅ Single FastAPI instance
app = FastAPI(title="AI Assistant Backend")

# ✅ Enable CORS for Electron frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Electron uses file://
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health check endpoint
@app.get("/")
def health_check():
    return {"status": "ok", "message": "Backend is running"}

# ✅ Chat endpoint
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    text = req.message.lower()

    intents = predict_intent(text)

    if intents:
        intent = intents[0]["intent"]

        # Execute task and return text reply
        task_result = map_task(intent, text)
        if task_result:
            return ChatResponse(
                reply=task_result,
                action=None,
                intent=intent
            )

        response = get_static_response(intent)
        if response:
            return ChatResponse(
                reply=response,
                action=None,
                intent=intent
            )

    # Gemini fallback
    return ChatResponse(
        reply=gemini_reply(text),
        action=None,
        intent="gemini"
    )
