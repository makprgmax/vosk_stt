from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json

model = Model("model-en")
rec = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    if rec.AcceptWaveform(indata):
        print(json.loads(rec.Result())["text"])
    else:
        print(json.loads(rec.PartialResult())["partial"])

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Recording...")
    while True:
        pass
