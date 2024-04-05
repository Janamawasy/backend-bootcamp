from utils.data_funcs import read_db
from fastapi import APIRouter, Depends
from auth.jwt_bearer import jwtBearer

router = APIRouter()

@router.get("/get-all-students", dependencies=[Depends(jwtBearer())])
def get_all_students():
    """
    :return: all students data in json file in dictionary
    """
    all_students = read_db('data/students_data.json')
    print(all_students)
    return {'message': 'Success', 'data': all_students}


@router.get("/get-student-by-id/{id}", dependencies=[Depends(jwtBearer())])
def get_student_by_id(id):
    """
    :param id: student id
    :return: student obj, when students[id] == id
    """
    all_students = read_db('data/students_data.json')
    student = all_students[id]
    print(student)
    return student


@router.get("/get-student-by-class/{class_name}", dependencies=[Depends(jwtBearer())])
def get_student_by_class(class_name):
    """
    :param class_name: class name
    :return: list of student names that have class_name
    """
    students_in_class = []
    all_students = read_db('data/students_data.json')
    for id in all_students:
        if class_name in all_students[id]["classes"]:
            students_in_class.append(all_students[id]["name"])
    print(students_in_class)
    return students_in_class
