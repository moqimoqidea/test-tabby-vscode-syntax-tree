# file name: server.py

import json
import logging
import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/v1/completions")
async def post_completion(request: Request):
    data = await request.json()
    # Assuming 'data' is a dictionary, log a message without logging the data directly
    logging.info(f"Received POST data: {json.dumps(data, indent=2)}")
    return {"message": "Data received", "yourData": data}

@app.get("/v1/health")
async def health_check():
    logging.info("Health check queried.")
    return JSONResponse(content={"status": "success", "message": "Service is up and running"}, status_code=200)

@app.options("/v1/health")
async def health_check_options():
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "*",
    }
    logging.info("Health check options queried.")
    return Response(status_code=204, headers=headers)

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("server:app", host=host, port=port)
