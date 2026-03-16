from typing import Any

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_role(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Person(\"{self.name}\", {self.age})"

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.id = student_id
        self.courses: list['Courses'] = []

    def get_role(self) -> str:
        return "Student"
    
    def enroll(self, course: 'Courses'):
        if course not in self.courses:
            self.courses.append(course)
    
    def __str__(self) -> str:
        return super().__str__()+f"ID:{self.id}"

class Professor(Person):
    def __init__(self, name: str, age: int, professor_id: str) -> None:
        super().__init__(name, age)
        self.id = professor_id
        self.department = None
        self.courses: list['Courses'] = []

    def get_role(self) -> str:
        return "Professor"
    
    def assign_to_course(self, course: 'Courses') -> None:
        if course not in self.courses:
            self.courses.append(course)

    def set_department(self, department: 'Department') -> None:
        self.department = department

    def __str__(self) -> str:
        if self.department:
            department_name: str = self.department.name
            return super().__str__()+f"ID: {self.id}, department: {self.department}"
        else:
            return super().__str__()+f"ID: {self.id}, department: Dipartimento ancora non assegnato"
    
class Courses:
    def __init__(self, name: str, code: str) -> None:
        self.course_name = name
        self.course_code = code
        self.students: list[Student] = []
        self.professor: Professor = None

    def add_student(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)
    
    def set_professor(self, professor: Professor) -> None:
        self.professor = professor

    def __str__(self) -> str:
        if self.professor:
            professor_name:str = self.professor.name 
            return f"Course name: {self.course_name}, ID: {self.course_code}, professor: {professor_name}"   # y put attr in var + reask una var se                                                                    ctrl a ferecuca                                       # almeno furbo che fa in dir xe | non copia nulla o clip
        else:
            return f"Course name: {self.course_name}, ID: {self.course_code}, professor: Non ancora assegnato"                                                                              # volendo | pure qua
       
class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.professors: list[Professor] = []
        self.courses: list[Courses] = []

    def add_courses(self, course: Courses) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def add_professor(self, professor: Professor) -> None:
        if professor not in self.professors:
            self.professors.append(professor)
    
    def __str__(self) -> str:
        return f"Department: {self.name}" # not dep_name cm cascio
    
class University:
    def __init__(self, name: str) -> None:
        self.name = name
        self.departments: list[Department] = []
        self.students: list[Student] = []
    
    def add_department(self, department:Department) -> None:
        self.departments.append(department)
    
    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def __str__(self) -> str:
        return f"University: {self.name}, Departments: {[d.name for d in self.departments]}, Students: {[s.name for s in self.students]}"























            # prof mno teahcer






            # tab no add new line but repl