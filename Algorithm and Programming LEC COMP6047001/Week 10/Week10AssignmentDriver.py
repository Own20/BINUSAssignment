from Week10Assignment import Student
from Week10Assignment import Teacher

namS = input("Name Student: ")
addS = input("Address Student: ")
couS = input("Courses Student: ")
graS = str(input("Grades Student: "))

namT = input("Name Teacher: ")
addT = input("Address Teacher: ")
couTA = input("Courses add: ")
couTR = input("Courses remove: ")

s = Student(namS, addS)

t = Teacher(namT, addT)

nameS = s.setName(namS)
addressS = s.setAddress(addS)
addCourseGradeS = s.addCourseGrade(couS, graS)
printGradeS = s.printGrades()

nameT = t.setName(namT)
addressT = t.setAddress(addT)
addCourseT = t.addCourse(couTA)
removeCourseT = t.removeCourse(couTR)

detailS = s.__str__()

detailT = t.__str__()

print(detailS)

print(detailT)