from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
app = FastAPI()
notes_with_id = {}
counter = 1

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Notes API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #f7f8fa;
                    color: #333;
                    text-align: center;
                    padding: 60px 20px;
                }
                h1 {
                    color: #222;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 18px;
                    margin-bottom: 30px;
                }
                a.button {
                    display: inline-block;
                    background-color: #0078D7;
                    color: white;
                    padding: 12px 24px;
                    border-radius: 8px;
                    text-decoration: none;
                    font-weight: bold;
                    margin-bottom: 40px;
                }
                a.button:hover {
                    background-color: #005fa3;
                }
                footer {
                    margin-top: 60px;
                    font-size: 14px;
                    color: #555;
                }
                footer a {
                    color: white;
                    background-color: #0078D7;
                    padding: 8px 16px;
                    border-radius: 6px;
                    text-decoration: none;
                    display: inline-block;
                    margin-top: 10px;
                }
                footer a:hover {
                    background-color: #005fa3;
                }
            </style>
        </head>
        <body>
            <h1>📝 Notes API</h1>
            <p>Create, read, update, and delete your notes easily.</p>
            <a href="/docs" class="button">Open Swagger UI</a>

            <footer>
                <p>Made with ❤️ by Sanidhy Chaturvedi</p>
                <a href="https://github.com/sanidhy-main" target="_blank">github.com/sanidhy-main</a>
            </footer>
        </body>
    </html>
    """

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
