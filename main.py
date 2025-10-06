from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
app = FastAPI()
notes_with_id = {}
counter = 1

@app.get("/", response_class=HTMLResponse)
def home():
    with open("mainpage.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/note")
def add_note(title: str, content: str):
    global counter
    note = {"Title": title, "Content": content}
    if not title or not content:
        raise HTTPException(status_code=404, detail="Title or Content cannot be empty")
    notes_with_id[counter] = note
    counter += 1
    return {counter-1: {title: content}}

@app.get("/notes")
def view_notes():
    return notes_with_id

@app.get("/notes/{note_id}")
def view_note(note_id: int):
    if note_id not in notes_with_id:
        raise HTTPException(status_code=404, detail="Note not found")
    else: return {note_id: notes_with_id[note_id]}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes_with_id:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes_with_id[note_id]
    return {"success": True, "message": "Note deleted"}

@app.put("/notes/{note_id}")
def update_note(note_id: int, title: str, content: str):
    if not title or not content:
        raise HTTPException(status_code=404, detail="Title or Content cannot be empty")
    if note_id not in notes_with_id:
        raise HTTPException(status_code=404, detail="Note not found")
    note = notes_with_id[note_id]
    note["Title"] = title
    note["Content"] = content
    return {note_id: {title: content}}
