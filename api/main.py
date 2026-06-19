from fastapi import FastAPI
from pydantic import BaseModel

from core.orchestrator import Orchestrator

app = FastAPI()

brain = Orchestrator()


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    return brain.process(
        query=request.message,
        user_id=request.user_id
    )