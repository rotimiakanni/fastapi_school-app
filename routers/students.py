from fastapi import APIRouter, HTTPException, Depends, File
from ..services.students import student_service
from ..schemas.students import Student
from typing import Annotated

student_router = APIRouter()

# students = [
#     {"first_name": "John", "last_name": "Doe", "age": 16},
#     {"first_name": "Matthew", "last_name": "Taiwo", "age": 20}
# ]

students = [
    Student(first_name="John", last_name="Doe", age=16),
    Student(first_name="Dorathy", last_name="Doe", age=16),
]

def check_token(token):
    if token != 'secret':
        raise HTTPException(status_code=403, detail='Token mismatch')

@student_router.get('', status_code=200)
def get_students():
    return students

@student_router.post('', status_code=201)
def create_student(student: Student):
    student = student_service.create_student(student)
    students.append(student)
    return {'messages': 'Student created successfully.', 'data': student}

@student_router.put('/{first_name}', status_code=200)
def edit_student(first_name: str, student_payload: Student):
    for student in students:
        if student.first_name == first_name:
            student.first_name = student_payload.first_name
            student.age = student_payload.age
            student.last_name = student_payload.last_name
            return {'message': 'Success', 'data': student}
    raise HTTPException(detail='Student not found.', status_code=404)
