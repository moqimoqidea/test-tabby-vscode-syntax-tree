# file name: server.py

import logging
import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Setup logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/v1/completions")
async def post_completion(request: Request):
    data = await request.json()
    # Assuming 'data' is a dictionary, log a message without logging the data directly
    logging.info(f"Received POST data: {data}")
    return {"message": "Data received", "yourData": data}

@app.get("/v1/health")
async def health_check():
    logging.info("Health check queried.")
    return JSONResponse(content={"status": "success", "message": "Service is up and running"}, status_code=200)

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("server:app", host=host, port=port)
