from ..schemas.students import Student

class StudentService:

    # @staticmethod
    # def create_student(first_name, last_name, age):
    #     return {
    #         'first_name': first_name, 
    #         'last_name': last_name, 
    #         'age': age
    #     }

    @staticmethod
    def create_student(student):
        return Student(
            first_name=student.first_name, 
            last_name=student.last_name, 
            age=student.age
        )
    
student_service = StudentService()