import askQuestion, addToDatabase, clearDatabase
from fastapi import FastAPI, UploadFile, File
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()
DATABASE_PATH = os.getenv("DATABASE_PATH")

@app.post("/ask")
def ask(prompt: str):
    response = askQuestion.predict(prompt)
    return response

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_location = f"{DATABASE_PATH}/{file.filename}"
    with open(file_location, "wb") as f:
        contents = await file.read()
        f.write(contents)
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}

@app.post("/add")
async def add():
    addToDatabase.main()
    return {"info": "Database updated successfully"}

@app.post("/clear")
async def clear():
    clearDatabase.clear_database()
    return {"info": "Database cleared successfully"}