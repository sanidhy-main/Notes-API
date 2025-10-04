from fastapi import FastAPI

app = FastAPI()

notes = {}

counter = 0
@app.post("/note")
def add_note(note: str):
    global counter
    notes[counter+1] = note
    counter += 1
    return {"Note": note}

@app.get("/notes")
def view_notes():
    return notes
