from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

class Request(BaseModel):
    text: str

app = FastAPI()

@app.post("/analyze")
async def analyze(req: Request):
    await asyncio.sleep(1)  # Симуляция запроса к LLM
    return {"intent": "greeting", "text": req.text}
