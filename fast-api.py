from fastapi import FastAPI
import pickle
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

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

# display all images in matched_faces folder in the browser
@app.get("/matched_faces/{filename}")
def get_matched_faces(filename: str):
    return FileResponse(f"matched_faces/{filename}")