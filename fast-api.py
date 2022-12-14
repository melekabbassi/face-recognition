from fastapi import FastAPI
import pickle
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
# upload file to server and save it in images folder (unknown_faces) to be used for face recognition
from fastapi import FastAPI, File, UploadFile
import shutil

matches = pickle.load(open("matches.pkl", "rb"))

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/matches")
def get_matches():
    return {"matches": matches}

# display all images in matched_faces folder in the browser using yield
@app.get("/matched_faces")
def get_matched_faces():
    for i in range(len(matches)):
        yield FileResponse(f"matched_faces/{i}.jpg")

@app.get("/matched_faces/{index}")
def get_matched_face(index: int):
    return FileResponse(f"matched_faces/{index}.jpg")

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f"unknown_faces/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}