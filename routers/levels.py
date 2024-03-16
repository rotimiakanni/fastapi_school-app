from fastapi import APIRouter, HTTPException, status
from ..schemas.students import Student
from ..services.levels import level_service
from ..schemas.levels import Level

level_router = APIRouter()

# without pydantic


levels = [
    {
        "name": "level_one", 
        "students": [
            {"first_name": "Matthew", "last_name": "Taiwo", "age": 20},
            {"first_name": "Paul", "last_name": "Taiwo", "age": 20}
        ]
    },

    {
        "name": "level_two", 
        "students": [
            {"first_name": "Joan", "last_name": "Peter", "age": 12},
        ]
    },
    
]

# @level_router.get('/')
# def get_levels():
#     return levels

# @level_router.get('/{level_name}')
# def get_level(level_name: str):
#     level = level_service.get_level(levels, level_name)
#     if level:
#         return {'message': 'success', 'data': level}
#     return {'message': 'success', 'data': level}

# @level_router.get('/{level_name}/students')
# def get_level_students(level_name: str):
#     level = level_service.get_level(levels, level_name)
#     return {'message': 'success', 'data': level.get('students', [])}

# @level_router.post('{level_name}/students')
# def add_students(level_name: str, first_name, last_name, age):
#     student = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'age': age
#     }
#     for level in levels:
#         if level.get('name') == level_name:
#             students = level.get('students')
#             students.append(student)
#             return {'message': 'success', 'data': level}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Level not found")
        

# with pydantic

levels: list[Level] = [
    Level(
        name="level_one", 
        students=[
            Student(first_name="John", last_name="Doe", age=16),
            Student(first_name="James", last_name="Musa", age=18),
        ]
    ),
    
]

@level_router.get('/')
def get_levels():
    return levels

@level_router.get('/{level_name}')
def get_level(level_name: str):
    level = level_service.get_level(levels, level_name)
    if level:
        return {'message': 'success', 'data': level}
    return {'message': 'success', 'data': level}

@level_router.get('/{level_name}/students')
def get_level_students(level_name: str):
    level = level_service.get_level(levels, level_name)
    return {'message': 'success', 'data': level.students if level else []}

@level_router.post('{level_name}/students')
def add_students(level_name: str, first_name, last_name, age):
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age
    }
    for level in levels:
        if level.name == level_name:
            students = level.students
            students.append(student)
            return {'message': 'success', 'data': level}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Level not found")
        