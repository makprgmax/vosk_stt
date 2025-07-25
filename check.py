from pydantic import BaseModel

class SpeechCommand(BaseModel):
    intent: str
    device: str
    location: str

data = {"intent": "turn_on", "device": "light", "location": "bedroom"}
cmd = SpeechCommand(**data)

print(cmd.device)  # light
