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

🚀 How to Run

Clone the repository:

```
git clone https://github.com/sanidhy-main/Notes-API.git
cd Notes-API
```

Install dependencies:

```
pip install fastapi uvicorn
```

Run the API server:

```
uvicorn main:app --reload
```

Open in your browser:

🌐 http://127.0.0.1:8000
 → for the custom homepage

⚙️ http://127.0.0.1:8000/docs
 → to explore and test the API using Swagger UI
4. Open http://127.0.0.1:8000/docs to explore the Swagger UI.
