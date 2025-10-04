from fastapi import FastAPI

app = FastAPI()

notes = {}
@app.post("/note")
def add_note(note: str):
    notes[1] = note
    return {"Note": note}

@app.get("/notes")
def view_notes():
    return notes
