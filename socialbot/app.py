from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running inside Chainlit!"}

@app.get("/status")
def get_status():
    return {"status": "ok"}
