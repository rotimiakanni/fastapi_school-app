from fastapi import FastAPI
from routers.students import student_router
from routers.levels import level_router
from middleware import add_process_time_header

app = FastAPI()

app.middleware("http")(add_process_time_header)

app.include_router(router=student_router, prefix='/students', tags=['Students'])
app.include_router(router=level_router, prefix='/levels', tags=['Levels'])

@app.get('/')
def index():
    return {"message": "Welcome to school!"}