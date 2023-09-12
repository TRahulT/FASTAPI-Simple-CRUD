from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Student(BaseModel):
    name: str
    rollno: int

students_db = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/students/", response_model=Student)
async def create_student(student: Student):
    students_db.append(student)
    return student

@app.get("/students/", response_model=List[Student])
async def get_students():
    return students_db

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    if student_id < len(students_db):
        return students_db[student_id]
    return {"error": "Student not found"}

@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, updated_student: Student):
    if student_id < len(students_db):
        students_db[student_id] = updated_student
        return updated_student
    return {"error": "Student not found"}

@app.delete("/students/{student_id}", response_model=Student)
async def delete_student(student_id: int):
    if student_id < len(students_db):
        deleted_student = students_db.pop(student_id)
        return deleted_student
    return {"error": "Student not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
