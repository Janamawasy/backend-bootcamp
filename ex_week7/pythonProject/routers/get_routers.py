from fastapi import APIRouter
import utils.db_funs as db_funs

router = APIRouter()

@router.get("/get-all-students")
async def get_all_students():
    all_students = await db_funs.read_db('data/students_data.json')
    print(all_students)
    return {'message': 'Success', 'data': all_students}


@router.get("/get-student-by-id/{id}")
async def get_student_by_id(id):
    all_students = await db_funs.read_db('data/students_data.json')
    student = all_students[id]
    return student


@router.get("/get-student-by-class/{class_name}")
async def get_student_by_class(class_name):
    students_in_class = []
    all_students = await db_funs.read_db('data/students_data.json')
    for id in all_students:
        if class_name in all_students[id]["classes"]:
            students_in_class.append(all_students[id]["name"])
    print('aaa')
    print(students_in_class)
    return students_in_class
