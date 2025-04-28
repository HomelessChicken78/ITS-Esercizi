class Room:
    '''The Room class represents a classroom.\n
    Each classroom has an ID (id), a floor (floor), a number of seats (seats) and an area (area).\n
    The area is calculated as double the seats.'''

    def __init__(self, id: str, floor: int, seats: int):

        #Check if the id is unique
        self.__id = id
        self.__floor = floor
        self.__seats = seats
        self.__area = seats*2
    
    def get_id(self) -> str:
        '''Returns the id of the room.'''
        return self.__id
    
    def get_floor(self) -> int:
        '''Returns the floor of the room.'''
        return self.__floor

    def get_seats(self) -> int:
        '''Returns the number of seats in the room.'''
        return self.__seats

    def get_area(self) -> int:
        '''Returns the area of the room.'''
        return self.__area
    
class Building:
    '''The Building class represents a building.\n
    Each building has a name (name), an address (address), a range of floors (floors), and a list of rooms (rooms).'''
    def __init__(self, name: str, address: str, floors: tuple, rooms: list[Room] = []):
        self.name = name
        self.address = address
        self.floors = floors

        self.__rooms = []
        for r in rooms:
            self.add_room(r)

    def get_floors(self):
        '''Returns the range of floors of the building.'''
        return self.floors

    def get_rooms(self) -> list[Room]:
        '''Returns the list of classrooms of the building'''
        return self.__rooms

    def add_room(self, room: Room) -> None:
        '''Adds a new classroom to the buidling, only if the floor of the classroom is between the range of floors of the building.'''
        if (room.get_floor() >= self.get_floors()[0] and room.get_floor() <= self.get_floors()[1]) and room.get_id() not in [stanza.get_id() for stanza in self.__rooms]:
            self.__rooms.append(room)

    def area(self) -> int:
        '''Returns the area of the building, by adding up the areas of all the classes'''
        tot: int = 0
        for r in self.get_rooms():
            tot += r.get_area()
        return tot

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

class Course:
    '''The class Course represent an accademic course.\n
    Each course has a name (name) and a list of groups (groups)'''
    def __init__(self, name):
        self.name = name
        self.groups = []
    
    def register(self, student: Student) -> None:
        '''Register a student in the first group avaible.\n
        A group is avaible when it still hasn't reached the limit of students.'''
        for g in self.groups:
            g: Group
            if (len(g.students) < g.limit) and student not in g.students:
                g.students.append(student)
                break


    def get_groups(self) -> list[Group]:
        '''Returns the list of groups in the course.'''
        return self.groups

    def add_group(self, group: Group) -> None:
        '''Add a group to the course.'''
        self.groups.append(group)