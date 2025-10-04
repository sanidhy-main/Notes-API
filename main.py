from fastapi import FastAPI

app = FastAPI()

notes_with_id = {}

counter = 1
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

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    del notes_with_id[note_id]

@app.put("/notes/{note_id}")
def update_note(note_id: int, title: str, content: str):
    note = notes_with_id[note_id]
    note["Title"] = title
    note["Content"] = content

