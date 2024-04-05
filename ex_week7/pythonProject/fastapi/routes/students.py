from fastapi import APIRouter, HTTPException, Request
import utils.db_funcs as db_fns
import utils.auth_fns as auth_fns
router = APIRouter()

@router.get("/students/")
async def read_students(request:Request):
    if auth_fns.check_token(request):
        school_json = db_fns.load_db()
        return school_json
    else:
        raise HTTPException(400, "no token")
@router.get('/students/{student_id}')
async def get_student_by_id(student_id:int):
    school_json = db_fns.load_db()
    if student_id in school_json:
        return school_json[student_id]
    else:
        return {"error":"student not found"}