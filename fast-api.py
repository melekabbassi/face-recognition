from fastapi import FastAPI
import pickle

matches = pickle.load(open("matches.pkl", "rb"))

app = FastAPI()
 
@app.get("/matches")
def get_matches():
    return {"matches": matches}