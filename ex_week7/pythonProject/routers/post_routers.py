from fastapi import APIRouter
from classes.student_class import Student
from utils.db_funs import read_db

router = APIRouter()

@router.post("/add-student")
def add_student(student: Student):
    filename = 'data/students_data.json'
    print(student)
    new_student = {
        "name": student.name,
        "id": student.id,
        "age": student.age,
        "classes": student.classes
    }
    print(new_student)
    # all_students = read_db(filename)
    # all_students[student.id] = new_student
    # if db_funs.save_db(all_students, filename):
    #     return {'massage': 'success'}
    # else:
    #     return {'massage': 'fail'}
