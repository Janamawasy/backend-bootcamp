from classes.student_class import Student
from utils.data_funcs import read_db, save_db
from fastapi import APIRouter, Depends
from auth.jwt_bearer import jwtBearer
from auth.manage_permitions import is_admin

router = APIRouter()


@router.post("/add-student", dependencies=[Depends(jwtBearer())])
def add_student(student: Student):
    """
    functiom add new student to students db in students_data.json file
    :param student: student class obj, has name, age, classes and id
    :return: {'massage': 'success' or 'fail'}
    """
    filename = 'data/students_data.json'
    print('student', student)
    new_student = {
        "name": student.name,
        "id": student.id,
        "age": student.age,
        "classes": student.classes
    }
    print('new_student', new_student)
    all_students = read_db(filename)
    all_students[student.id] = new_student
    print("all_students", all_students)
    res = save_db(all_students, filename)
    if res:
        return {'massage': 'success'}
    else:
        return {'massage': 'fail'}



# post request:
# Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/add-student -Body "name=name1, age=20, id=id_2, classes = [A,Z,Q]"
# Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/add-student -Body '{"name":"John Doe", "id":"id_2", "age":25, "classes":["A", "Z", "Q"]}' -ContentType "application/json"
