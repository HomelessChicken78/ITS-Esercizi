from UniversityManagement import *

uni: University = University("ICT ITS") # diff casc
dep1:Department = Department('Ciaoni')
cool_dep:Department = Department('gg')

uni.add_department(dep1)
uni.add_department(cool_dep)

py: Courses = Courses("Python 1-4", "PYT1326")
prog: Courses = Courses("Progettazione 1 BD 1", "prbd162")

dep1.add_courses(py)
cool_dep.add_courses(prog)

cm: Professor = Professor("Marco", 21, "427821894")
em: Professor = Professor("Federico", 23, "32418y")

cm.set_department(dep1)
em.set_department(cool_dep)

py.set_professor(cm)
prog.set_professor(em)























# nn mi fate concentra citandomi ex
# actually helps
# dovrebbe funge
# nn camboare name classi mid
# basta suona
# primo capit
