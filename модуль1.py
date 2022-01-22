from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model("./model")

def working_query(query):
	#, "дарова", "здравия желаю", "добрый вечер", "прив", "здарова", "добрый день"
    que = { ("привет", "здравствуй") : welcome}
    for i in query:
        for j in que:
            if i in j:
                que[j](query)
    if query == que:
        print("Привет")
    print(query)
    worker()
    
def worker():
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
    stream.start_stream()
    rec = KaldiRecognizer(model, 16000)
    while True:
        name_bot = "вася"
        data = stream.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            text = json.loads(rec.Result())["text"].split()
            print(text)
            for i in range(len(text)):
                if text[i] == name_bot:
                    working_query(text[i + 1:])
                    break
worker()
