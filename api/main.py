from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

# Wrap FastAPI app with Mangum for compatibility with Vercel
handler = Mangum(app)
