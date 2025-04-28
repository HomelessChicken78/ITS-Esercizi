from part1 import *
from part2 import *

# stanza1: Room = Room("ciao", 0, 20)
# #stanza1: Room = Room("ciao", 4, 2)  #Test for repeated id

# #test con i metodi get
# print(stanza1.get_id())
# print(stanza1.get_floor())
# print(stanza1.get_seats())
# print(stanza1.get_area())

# stanza2: Room = Room("A404c12", 0, 20)
# stanza3: Room = Room("QJFI9y7", 1, 20)
# stanza4: Room = Room("loGu3ds", 1, 20)
# stanza5: Room = Room("Uloo00", 1, 20)
# stanza6: Room = Room("Pn372HNd74nH8", 2, 20)
# stanzaImpossibile1: Room = Room("QQQQQQ666", 100, 20)
# stanzaImpossibile2: Room = Room("RRRRRR666", 100, 20)

# building1: Building = Building("Sede 1", "Viale Cesare Pavese, 305", (0, 2), [stanza1, stanza2, stanza3, stanza4, stanza5, stanza6, stanzaImpossibile1])
# print([r.get_id() for r in building1.get_rooms()])

# building1.add_room(stanzaImpossibile2)
# print([r.get_id() for r in building1.get_rooms()])

# building1.add_room(stanza1)
# print([r.get_id() for r in building1.get_rooms()])

# print(building1.area())

# # Creating instances for students
# cc: Student = Student("ccst03", "Cristiano", "C", 21)
# cr: Student = Student("crssd", "Cristiano", "Ronaldo", 40)
# s0: Student = Student("std000", "Alice", "Aura", 20)
# s1: Student = Student("std001", "Bob", "Beast", 22)
# s2: Student = Student("std002", "Charlie", "Confusion", 18)
# s3: Student = Student("std003", "David", "Detective", 28)
# s4: Student = Student("std004", "Eve", "Evil", 25)
# s5: Student = Student("std005", "Frank", "Flower", 33)
# s6: Student = Student("std006", "Grace", "Gentle", 29)
# s7: Student = Student("std007", "Heidi", "Head", 19)
# s8: Student = Student("std008", "Ivan", "Insti", 37)
# s9: Student = Student("std009", "Judy", "Jelly", 21)
# s10: Student = Student("std010", "Marley", "Medium", 31)
# s11: Student = Student("std011", "Niaj", "Nightmare", 24)
# s12: Student = Student("std012", "Olivia", "Oliva", 19)
# s13: Student = Student("std012", "Paol", "Priest", 25)
# s14: Student = Student("std012", "Quasimodo", "Qui", 23)
# s15: Student = Student("std012", "Raul", "Ritu", 22)

# # Creating instances for lecturers
# fm: Lecturer = Lecturer("frcm96", "Federico", "M", 29)
# mr: Lecturer = Lecturer("mmsmedy", "Mario", "Rossi", 20)

# print("Creating a group and testing the limit of lecturers: ")
# gr1: Group = Group("Testing Group", 16)
# print(gr1.get_limit_lecturers())

# # Adding a student to the group
# gr1.add_student(s0)

# print("\nTesting if the student is now in that group: ")
# print(s0.group)
# for std in gr1.get_students():
#     print(std.name)

# print("\nAdd a lot of students to see if the limit is respected: ")
# gr1.add_student(s1)
# gr1.add_student(s2)
# gr1.add_student(s3)
# gr1.add_student(s4)
# gr1.add_student(s5)
# gr1.add_student(s6)
# gr1.add_student(s7)
# gr1.add_student(s8)
# gr1.add_student(s9)
# gr1.add_student(s10)
# gr1.add_student(s11)
# gr1.add_student(s12)
# gr1.add_student(s13)
# gr1.add_student(s14)
# gr1.add_student(s15)
# gr1.add_student(cc)
# for std in gr1.get_students():
#     print(std.name)

# print("\nTrying to add the same student twice: ")
# gr2 = Group("Test 2", 3)
# gr2.add_student(s0)
# print(s0.group)
# gr2.add_student(s0)
# for std in gr2.get_students():
#     print(std.name)

# print(f"\nAdding two lecturer even if the limit is {gr2.get_limit_lecturers()}:")
# gr2.add_lecturer(fm)
# gr2.add_lecturer(mr)
# for lect in gr2.lecturers:
#     print(lect.name)

from part3 import *
# Creating instances for students
cc: Student = Student("ccst03", "Cristiano", "C", 21)
cr: Student = Student("crssd", "Cristianoh", "Ronaldo", 40)
s0: Student = Student("std000", "Alice", "Aura", 20)
s1: Student = Student("std001", "Bob", "Beast", 22)
s2: Student = Student("std002", "Charlie", "Confusion", 18)
s3: Student = Student("std003", "David", "Detective", 28)
s4: Student = Student("std004", "Eve", "Evil", 25)
s5: Student = Student("std005", "Frank", "Flower", 33)
s6: Student = Student("std006", "Grace", "Gentle", 29)
s7: Student = Student("std007", "Heidi", "Head", 19)
s8: Student = Student("std008", "Ivan", "Insti", 37)
s9: Student = Student("std009", "Judy", "Jelly", 21)
s10: Student = Student("std010", "Marley", "Medium", 31)
s11: Student = Student("std011", "Niaj", "Nightmare", 24)
s12: Student = Student("std012", "Olivia", "Oliva", 19)
s13: Student = Student("std012", "Paol", "Priest", 25)
s14: Student = Student("std012", "Quasimodo", "Qui", 23)
s15: Student = Student("std012", "Raul", "Ritu", 22)

# Creating instances for lecturers
fm: Lecturer = Lecturer("frcm96", "Federico", "M", 29)
mc: Lecturer = Lecturer("cmcr98", "Marco", "C", 27)
lp: Lecturer = Lecturer("plrd00", "Leonardo", "P", 25)
fg: Lecturer = Lecturer("gfvl01", "Flavio", "G", 24)

# Creating the groups
gr1: Group = Group("I tre moschettieri", 3)
gr2: Group = Group("I cinque nani", 5)
gr3: Group = Group("Testing group", 11)

#Creating the course
cloud: Course = Course("ITS Cloud 2025")

print("Adding the groups to the course: ")
cloud.add_group(gr1)
cloud.add_group(gr2)
cloud.add_group(gr3)
for g in cloud.get_groups():
    print(g.name)

print("\nRegistering multiple students: ")
cloud.register(cc)
cloud.register(cr)
cloud.register(s0)
cloud.register(s1)
cloud.register(s2)
cloud.register(s3)
cloud.register(s4)
cloud.register(s5)
cloud.register(s6)
cloud.register(s7)
cloud.register(s8)
cloud.register(s9)
cloud.register(s10)
cloud.register(s11)
cloud.register(s12)
cloud.register(s13)
cloud.register(s14)
cloud.register(s15)
for g in cloud.get_groups():
    print("\n", g.name)
    for std in g.get_students():
        print(std.name)