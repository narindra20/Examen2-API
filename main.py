from fastapi import FastAPI

app = FastAPI()

@app.get("/ping", response_description="Réponse avec 'pong'")
def ping():
    return "pong"
