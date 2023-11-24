import uvicorn
from fastapi import FastAPI, File, UploadFile, status, Header, Request, Depends
from fastapi.staticfiles import StaticFiles
app = FastAPI()

count = 0

@app.get("/")
async def getR():
    return "Test"

@app.get("/get")
async def getUser(sum: int):
    global count
    count += sum
    return {"count":count}
