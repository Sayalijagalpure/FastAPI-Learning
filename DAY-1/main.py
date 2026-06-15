from fastapi import FastAPI
# using 3 GET endpoints
app = FastAPI()

@app.get("/")
def home():
    return {"message": "This is my first FastAPI project"}

@app.get("/student/{student_id}/{student_name}")
def get_student(student_id: int, student_name: str):
    return{
        "Student ID": student_id,
        "Name": student_name
    }

@app.get("/search")
def search_student(name: str, age: int):
    return{
        "Name": name,
        "age": age
    }