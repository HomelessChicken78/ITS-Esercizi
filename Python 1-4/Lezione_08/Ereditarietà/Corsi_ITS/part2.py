class Person:
    '''Represent a person. It has a fiscal code, a name, a surname and an age'''
    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
    
    def get_cf(self) -> str:
        '''Returns the fiscal code of the person.'''
        return self.cf

    def get_name(self) -> str:
        '''Returns the name of the person.'''
        return self.name

    def get_surname(self) -> str:
        '''Returns the surname of the person.'''
        return self.surname
    
    def get_age(self) -> int:
        '''Returns the age of the person.'''
        return self.age

class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)

        self.group = None
    
    def set_group(self, group):
            self.group = group

class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)

class Group:
    '''The class Group represent a group of study.\n
    Each group has a name, a limit of students, a list of students and a list of lecturers'''
    def __init__(self, name: str, limit: int):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
    
    def get_name(self) -> str: 
        '''Returns the name of the group'''
        return self.name

    def get_limit(self) -> int: 
        '''Returns the group's limit.'''
        return self.limit

    def get_students(self) -> list[Student]: 
        '''Returns a list containing all students'''
        return self.students

    def get_limit_lecturers(self) -> int:
        '''Returns the group teachers' limit.\n
        It is allowed 1 teacher every 10 students.\n
        This limit is at least set to 1 teacher, even if there are less than 10 students'''
        return (self.limit // 10) + 1

    def add_student(self, student: Student) -> None: 
        '''Adds a studenent to the group, if the limit of students has not been reached yet'''
        if (len(self.students) < self.limit) and student not in self.students:
            self.students.append(student)
            # student.set_group(self.name)
            student.set_group(self)

    def add_lecturer(self, lecturer: Lecturer) -> None: 
        '''Adds a teacher to the group, if the limit of the teachers has not been reached yet'''
        if (len(self.lecturers) < self.get_limit_lecturers()) and lecturer not in self.lecturers:
            self.lecturers.append(lecturer)