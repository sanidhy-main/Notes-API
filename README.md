# Notes API

A simple CRUD Notes API built with **FastAPI**. This project demonstrates a functional backend API with full create, read, update, and delete operations, along with basic error handling.

---

## Features
- **Create notes** with title and content (`POST /note`)  
- **Read notes**  
  - View all notes (`GET /notes`)  
  - View a note by ID (`GET /notes/{note_id}`)  
- **Update notes** by ID (`PUT /notes/{note_id}`)  
- **Delete notes** by ID (`DELETE /notes/{note_id}`)  
- **Error handling** for empty inputs and invalid/non-existent IDs

---

## Technologies
- **Python**  
- **FastAPI**  
- **Swagger UI** (automatic API docs)

---

## How to Run
1. Clone the repository:  
```
git clone <your-repo-url>
```

2. Navigate into the folder and install dependencies:
```
pip install fastapi uvicorn
```

3. Run the API server:
```
uvicorn main:app --reload
```

4. Open http://127.0.0.1:8000/docs to explore the Swagger UI.
