from fastapi import FastAPI

app = FastAPI()

notes_with_id = {}

counter = 0
@app.post("/note")
def add_note(title: str, content: str):
    global counter
    note = {"Title": title, "Content": content}
    notes_with_id[counter] = note
    counter += 1
    return {counter-1: {title: content}}

@app.get("/notes")
def view_notes():
    return notes_with_id

@app.get("/notes/{note_id}")
def view_note(note_id: int):
    return f"{note_id}: {notes_with_id[note_id]}"

